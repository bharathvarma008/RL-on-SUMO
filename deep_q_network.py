import torch
from torch import nn

class DQN(nn.Module):
    '''
    This class implements deep q network with pytorch
    '''
    def __init__(self, inputs, outputs, layers=[128, 64, 16]):
        super(DQN, self).__init__()

        # TODO: layers will be a list [A, B, C] on layer sizes.
        # TODO: implement the initialization of the deep net so it will
        # TODO: be in such shape: [inputs, A, B, C, outputs].
        # self.module_list = []
        # for idx, n in enumerate(layers):
        #     if idx==0: # if it's first layer
        #         self.module_list.append(nn.Linear(inputs, n))
        #     elif idx==len(layers)-1: # if its last layer.
        #         self.module_list.append(nn.Linear(n, outputs))
        #         break
        #     else:
        #         self.module_list.append(nn.Linear(layers[idx-1], layers[idx]))
        #     self.module_list.append(nn.ReLU())
        # #
        # # self.model = nn.Sequential(*layers_list)

        self.fc1 = nn.Linear(inputs, 128)
        self.relu1 = nn.ReLU()
        self.fc2 = nn.Linear(128, 64)
        self.relu2 = nn.ReLU()
        self.fc3 = nn.Linear(64, 16)
        self.relu3 = nn.ReLU()
        self.head = nn.Linear(16, outputs)


    def forward(self, x):
        x = self.relu1(self.fc1(x))
        x = self.relu2(self.fc2(x))
        x = self.relu3(self.fc3(x))
        return self.head(x.view(x.size(0), -1))
