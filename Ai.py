import torch
class Ai(torch.nn.Module):
    def __init__(self, inputs=3):
        super(Ai, self).__init__()
        self.l1 = torch.nn.Linear(inputs, 1)

    def forward(self, x):
        """
        :param x: tensor de dimesiones (3,1)
        :return: tensor de dimesiones (1,1)
        """
        return torch.sigmoid(self.l1(x))

    def get_genomas(self):
        """"
        :return: pesos, bias
        """
        return self.l1.weight, self.l1.bias