# AudioFingerprintModel
2 process have done in this project:
1. data collection
2. make model to use for generate fingerprint of audio
## DataSet
get 13281 songs from youtube (choose ids from [YouTube-music-video-5M project](https://github.com/keunwoochoi/YouTube-music-video-5M) randomly)<br />
extract chromagram feature from songs and save them<br />
you can access the [dataset](https://drive.google.com/drive/folders/134RktD8wmU9JZtqBinw6invJg2GFu5AH?usp=sharing)
(train and test file for preprocced data)
## Model
train the lstm autoencoder model for generate the 24-bit fingerprint for per sec
