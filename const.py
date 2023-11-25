import torch
import torch.nn as nn
import torch.nn.functional as F


class Decoder(nn.Module):
    """
    Décode le vecteur latent et renvoie les données reconstruites
    """

    def __init__(self):
        super(Decoder, self).__init__()
        # Couches convolutives
        self.conv1 = nn.Conv2d(1, 16, kernel_size=5, stride=1, padding=2)  # (1, 16, 1, 25)
        self.convbatchNorm1 = nn.BatchNorm2d(16)
        self.upsampling1 = nn.Upsample(size=(1, 250))  # (1, 16, 1, 250)
        self.ConvUp1 = nn.ConvTranspose2d(16, 8, kernel_size=1, stride=1)  # (1, 8, 1, 250)
        self.ConvUp2 = nn.ConvTranspose2d(8, 1, kernel_size=1, stride=1)  # (1, 1, 1, 250)
        # Couches denses
        self.dense1 = nn.Linear(25, 25)
        self.dense2 = nn.Linear(25, 125)
        self.dense3 = nn.Linear(125, 250)
        # concaténation
        self.concatDense1 = nn.Linear(500, 250)

    def forward(self, z):
        # Couches convolutives
        z_conv = z.reshape((1, 25)).unsqueeze(0).unsqueeze(0)
        z_conv = F.relu(self.convbatchNorm1(self.conv1(z_conv)))
        z_conv = self.upsampling1(z_conv)
        z_conv = self.ConvUp1(z_conv)
        z_conv = self.ConvUp2(z_conv)
        z_conv = z_conv.flatten()
        # Couches denses
        z_dense = self.dense1(z)
        z_dense = F.relu(self.dense2(z_dense))
        z_dense = F.relu(self.dense3(z_dense))
        z_dense = z_dense.flatten()
        # Concaténation
        z_dense = torch.cat((z_conv, z_dense), 0)
        # Dernières couches denses
        z_final = self.concatDense1(z_dense)
        z_final = z_final.reshape(1, 250)
        return z_final


categories_to_full_name = {'NOR': 'Normal beat (NOR)',
                           'LBBB': 'Left bundle branch block beat (LBBB)',
                           'RBBB': 'Right bundle branch block beat (RBBB)',
                           'NE': 'Nodal (junctional) escape beat (NE)',
                           'AP': 'Atrial premature beat (AB)',
                           'aAP': 'Aberrated atrial premature beat (aAP)',
                           'NP': 'Nodal (junctional) premature beat (NP)',
                           'PVC': 'Premature ventricular contraction (PVC)',
                           'VE': 'Ventricular escape beat (VE)',
                           'fVN': 'Fusion of ventricular and normal beat (VF)',
                           }
