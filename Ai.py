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
        devuelve un tensores modificables para pesos y bias
        :return: clon de peso y bias
        :rtype: (torch.Tensor, torch.Tensor)
        """
        return self.l1.weight.clone(), self.l1.bias.clone()

    def export_to_onnx(self, file_name):
        """
        Exporta el modelo a formato ONNX
        :param file_name: Nombre del archivo ONNX
        :type file_name: str
        """
        dummy_input = torch.tensor([[0.5, 1, 0.5]], dtype=torch.float)
        torch.onnx.export(self, dummy_input, file_name, input_names=['input'], output_names=['output'])
        print(f"Modelo guardado en formato ONNX como {file_name}")