import torch
import torch.nn as nn
from torchvision.models import mobilenet_v2
from torchvision.models.mobilenetv2 import ConvBNActivation

class CustomMobileNetV2(nn.Module):
    def __init__(self, in_channels=1, num_classes=1):
        super(CustomMobileNetV2, self).__init__()
        
        # Load pretrained MobileNetV2
        self.model = mobilenet_v2(pretrained=True)
        
        # Modify first convolution layer to accept grayscale input
        self.model.features[0][0] = ConvBNActivation(
            in_channels,  # Changed from 3 to 1 for grayscale
            32,
            kernel_size=3,
            stride=2,
            groups=1,
            norm_layer=nn.BatchNorm2d,
            activation_layer=nn.ReLU6
        )
        
        # Modify classifier for binary classification
        self.model.classifier = nn.Sequential(
            nn.Dropout(p=0.2),
            nn.Linear(self.model.last_channel, num_classes)
        )
        
        # Initialize the new layers
        self._initialize_weights()
    
    def _initialize_weights(self):
        for m in self.modules():
            if isinstance(m, nn.Conv2d):
                nn.init.kaiming_normal_(m.weight, mode='fan_out')
                if m.bias is not None:
                    nn.init.zeros_(m.bias)
            elif isinstance(m, nn.BatchNorm2d):
                nn.init.ones_(m.weight)
                nn.init.zeros_(m.bias)
            elif isinstance(m, nn.Linear):
                nn.init.normal_(m.weight, 0, 0.01)
                nn.init.zeros_(m.bias)
    
    def forward(self, x):
        # Handle single channel input
        if x.size(1) == 1:
            x = x.repeat(1, 1, 1, 1)  # Repeat single channel
        
        x = self.model.features(x)
        x = nn.functional.adaptive_avg_pool2d(x, (1, 1))
        x = torch.flatten(x, 1)
        x = self.model.classifier(x)
        return x
