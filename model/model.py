import torch.nn as nn
import torch.nn.functional as F
import torch


class Net(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(2, 8, kernel_size=3, padding=(1,1))
        torch.nn.init.xavier_uniform_(self.conv1.weight)
        self.bn1 = nn.BatchNorm2d(num_features=8)
        self.conv2 = nn.Conv2d(8, 8, kernel_size=3, padding=(1,1))
        self.bn2 = nn.BatchNorm2d(num_features=8)
        self.conv3 = nn.Conv2d(8, 8, kernel_size=3, stride=2, padding=(1,1))
        self.bn3 = nn.BatchNorm2d(num_features=8)
        self.conv4 = nn.Conv2d(8, 16, kernel_size=3, padding=(1,1))
        self.bn4 = nn.BatchNorm2d(num_features=16)
        self.conv5 = nn.Conv2d(16, 16, kernel_size=3, stride=2, padding=(1,1))
        self.bn5 = nn.BatchNorm2d(num_features=16)
        self.conv6 = nn.Conv2d(16, 32, kernel_size=3, padding=(1,1))
        self.bn6 = nn.BatchNorm2d(num_features=32)
        self.conv7 = nn.Conv2d(32, 32, kernel_size=3, stride=2, padding=(1,1))
        self.bn7 = nn.BatchNorm2d(num_features=32)
        self.conv8 = nn.Conv2d(32, 64, kernel_size=3, padding=(1,1))
        self.bn8 = nn.BatchNorm2d(num_features=64)
        self.conv9 = nn.Conv2d(64, 64, kernel_size=3, stride=2, padding=(1,1))
        self.bn9 = nn.BatchNorm2d(num_features=64)
        self.conv10 = nn.Conv2d(64, 128, kernel_size=3, padding=(1,1))
        self.bn10 = nn.BatchNorm2d(num_features=128)
        self.conv11 = nn.Conv2d(128, 128, kernel_size=3, stride=2, padding=(1,1))
        self.bn11 = nn.BatchNorm2d(num_features=128)
        self.conv12 = nn.Conv2d(128, 256, kernel_size=3, padding=(1,1))
        self.bn12 = nn.BatchNorm2d(num_features=256)
        self.deconv1 = nn.ConvTranspose2d(256, 512, kernel_size=3, stride=2, padding=(1,1))
        self.bn13 = nn.BatchNorm2d(num_features=512)
        self.conv13 = nn.Conv2d(512, 128, kernel_size=3, padding=(1,1))
        self.bn14 = nn.BatchNorm2d(num_features=128)
        self.deconv2 = nn.ConvTranspose2d(128, 128, kernel_size=3, stride=2, padding=(1,1))
        self.bn15 = nn.BatchNorm2d(num_features=128)
        self.conv14 = nn.Conv2d(128, 64, kernel_size=3, padding=(1,1))
        self.bn16 = nn.BatchNorm2d(num_features=64)
        self.deconv3 = nn.ConvTranspose2d(64, 64, kernel_size=3, stride=2, padding=(1,1))
        self.bn17 = nn.BatchNorm2d(num_features=64)
        self.conv15 = nn.Conv2d(64, 32, kernel_size=3, padding=(1,1))
        self.bn18 = nn.BatchNorm2d(num_features=32)
        self.deconv4 = nn.ConvTranspose2d(32, 32, kernel_size=3, stride=2, padding=(1,1))
        self.bn19 = nn.BatchNorm2d(num_features=32)
        self.conv16 = nn.Conv2d(32, 16, kernel_size=3, padding=(1,1))
        self.bn20 = nn.BatchNorm2d(num_features=16)
        self.deconv5 = nn.ConvTranspose2d(16, 16, kernel_size=3, stride=2, padding=(1,1))
        self.bn21 = nn.BatchNorm2d(num_features=16)
        self.conv17 = nn.Conv2d(16, 8, kernel_size=3, padding=(1,1))
        self.bn22 = nn.BatchNorm2d(num_features=8)
        self.conv18 = nn.Conv1d(8, 2, kernel_size=(1, 1))


    def forward(self, x):
        x_1 = F.relu(self.bn1(self.conv1(x.double())))
        x_2 = F.relu(self.bn2(self.conv2(x_1)))
        x_3 = F.relu(self.bn3(self.conv3(x_2)))
        x_4 = F.relu(self.bn4(self.conv4(x_3)))
        x_5 = F.relu(self.bn5(self.conv5(x_4)))
        x_6 = F.relu(self.bn6(self.conv6(x_5)))
        x_7 = F.relu(self.bn7(self.conv7(x_6)))
        x_8 = F.relu(self.bn8(self.conv8(x_7)))
        x_9 = F.relu(self.bn9(self.conv9(x_8)))
        x_10 = F.relu(self.bn10(self.conv10(x_9)))
        x_11 = F.relu(self.bn11(self.conv11(x_10)))
        x_12 = F.relu(self.bn12(self.conv12(x_11)))
        x_13 = F.relu(self.bn13(self.deconv1(x_12, output_size=[2,13])))
        x_14 = F.relu(self.bn14(self.conv13(x_13)))
        x_14 = torch.add(x_14, x_10)
        x_15 = F.relu(self.bn15(self.deconv2(x_14, output_size=[4, 26])))
        x_16 = F.relu(self.bn16(self.conv14(x_15)))
        x_16 = torch.add(x_16, x_8)
        x_17 = F.relu(self.bn17(self.deconv3(x_16, output_size=[8,51])))
        x_18 = F.relu(self.bn18(self.conv15(x_17)))
        x_18 = torch.add(x_18, x_6)
        x_19 = F.relu(self.bn19(self.deconv4(x_18, output_size=[16,101])))
        x_20 = F.relu(self.bn20(self.conv16(x_19)))
        x_20 = torch.add(x_20, x_4)
        x_21 = F.relu(self.bn21(self.deconv5(x_20, output_size=[31, 201])))
        x_22 = F.relu(self.bn22(self.conv17(x_21)))
        x_22 = torch.add(x_22, x_2)
        x_23 = F.relu(self.conv18(x_22))
        x_24 = F.softmax(x_23, dim=1)
        return x_24
