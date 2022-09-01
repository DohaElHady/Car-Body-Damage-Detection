![Results](https://github.com/DohaElHady/CarBodyDamageDetection/blob/main/Results/PredResults.png)

Stopping training early as no improvement observed in last 100 epochs. Best results observed at epoch 22, best model saved as best.pt.

123 epochs completed in 0.387 hours.
Optimizer stripped from runs/train/exp2/weights/best.pt, 173.2MB

Model summary: 444 layers, 86173414 parameters, 0 gradients, 203.8 GFLOPs
                 Class     Images  Instances          P          R     mAP@.5 mAP@.5:.95: 100% 1/1 [00:00<00:00,  2.25it/s]
                   all         10         28      0.304      0.393      0.249      0.104
