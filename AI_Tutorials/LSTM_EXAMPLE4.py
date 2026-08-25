#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 04:51:52 2026

@author: apm
"""

'''

Signal processing 


when we hear voice, it is actually continous signal and

like Amplitude = f(time)

this is analog, and computer how save?

microphone first convert change of air pressure to eelctrical signals
and then one ADC to digital

so e have two thing


1- Sampling
it means for insatnce sample rate : 16000 Hz which means
16000 measurement per seconds from wave

so if we have one 5 scond files, we have 5*160000=80000 samples
which si array we called waveform



2- Bit depth
the value fo amplitude for each measurement with which accuracy we save

form 8 bit, 16 bit and ...
in 16 Bits PCM one sample is inteegr betwen 
-32768 to 32767




3-Channel
the audo can be different channel
for insatnce

Mono --> 
time →
[0.1, 0.2, 0.4, 0.3, ...]


Sterep-->
         time →
Left:   [0.1, 0.2, 0.4, ...]
Right:  [0.2, 0.1, 0.3, ...]



so we have 4 feature of one digital audio
Audio
 ├── Waveform / Samples
 ├── Sample Rate
 ├── Bit Depth
 └── Channels
 
 
 
 
so we have different format for audio
.wav , .p3, .flac , .aac , .m4a , .ogg



Audio
|
|----Uncompressed (WAV / AIFF )
|
|---Losslesss compress (FLAC / ALAC)
|
|---lOSSY COMPRESSED (mp3, aac , opus)




wav IS MOST known for isgnal procesing and ML



MP3 actualy is lossy compresion, the infromatoion
so if wav is 50mb, mp4 is multipel mb

so mp3 must eb decoder to PCM smapel and then waveform




also flac it has compresion but it is lsosless

original pcm --> flac smaller file-->decode exact original pcm
so instead of mp3, teh informationd oesnt lose.



so in Deep learning, the files are MP3, WAV , FLAC
so we decode them to waveform and numbers

but we have two main approachs


1- RAW Waveform
we can give waveform to neural newtork diretcly 

some models liek wav2vect


2- Feature Extraction
in more classic and we short-time analysis -_>spectorgram -->
mel spectrogram and then MFCC and tehh LSTM


short time --> audio to smaller parts , for instance form 1 second
to multiple ms .

and we do window FFT , instead of FFT on whoel audio
each frame on FFT

now we have also information of time an dfrequency

             TIME →
Frequency
↑
|
|       ███
|   ██  ███
| █████ ██
| ██  █████
|


x = time, y=frequency, color/intensity = energy

spectrogram said that , in each second, which frequency with which intencity.


it is more usefull and information rather than raw waveform.



so MEL Spectrogram what is this? our ear doesnt frequence lienar
the 100 hz to 200 hz is different perception and more important than
10 000 and 10 100 HZ, 
so we must from frequecny go to Mel scale that eb better close
to human erception.



in speech recognition, they found, it is not necessary to keep all
details of mel spectrogram and we can have compres ereprsentation

Waveform
   ↓
STFT
   ↓
Spectrogram
   ↓
Mel Filters
   ↓
Log
   ↓
DCT
   ↓
MFCC







                 REAL WORLD

                 Sound wave
                     ↓
                 Microphone
                     ↓
                    ADC
                     ↓
          Digital Audio Samples
                     ↓
        ┌────────────┴────────────┐
        ↓                         ↓
      WAV                       MP3
   PCM samples              compressed
        │                         │
        └────────────┬────────────┘
                     ↓
                   Decode
                     ↓
                  Waveform
                     ↓
       [0.01, 0.04, -0.02, ...]
                     ↓
              Signal Processing
                     ↓
        Spectrogram / Mel / MFCC
                     ↓
                   LSTM
                     ↓
             "YES" / "NO" / ...
             
            
    
            
    
    
    
so nstead of each frame has 80 mEL VALUES, we can have 13 MFCCC Corefficients

so ineatd of waveform (16000,) we can have MFCC (98,13) which is
98 time framces x 13 feature sper frame.



'''




# ============================================================
# Keyword Recognition with PyTorch LSTM
# Google Speech Commands + MFCC
# ============================================================


# ============================================================
# 1. Imports
# ============================================================

import torch
import torch.nn as nn
import torch.nn.functional as F

import torchaudio

from torch.utils.data import (
    Dataset,
    DataLoader,
    random_split
)

import matplotlib.pyplot as plt

from sklearn.metrics import (
    confusion_matrix,
    classification_report
)

import numpy as np


# ============================================================
# 2. Reproducibility
# ============================================================

torch.manual_seed(42)
np.random.seed(42)


# ============================================================
# 3. Commands
# ============================================================

COMMANDS = [
    "yes",
    "no",
    "up",
    "down",
    "left",
    "right",
    "on",
    "off",
    "stop",
    "go"
]


label_to_index = {

    label: i

    for i, label
    in enumerate(COMMANDS)

}


index_to_label = {

    i: label

    for label, i
    in label_to_index.items()

}


print(label_to_index)


# ============================================================
# 4. Device
# ============================================================

if torch.cuda.is_available():

    device = torch.device(
        "cuda"
    )

elif torch.backends.mps.is_available():

    device = torch.device(
        "mps"
    )

else:

    device = torch.device(
        "cpu"
    )


print(
    "Device:",
    device
)


# ============================================================
# 5. Download Google Speech Commands
# ============================================================

speech_dataset = torchaudio.datasets.SPEECHCOMMANDS(

    root="./data",

    download=True

)


print(
    "Total samples:",
    len(speech_dataset)
)


# ============================================================
# 6. Check one example
# ============================================================

(
    waveform,
    sample_rate,
    label,
    speaker_id,
    utterance_number

) = speech_dataset[0]


print(
    "Waveform shape:",
    waveform.shape
)

print(
    "Sample rate:",
    sample_rate
)

print(
    "Label:",
    label
)

print(
    "Speaker:",
    speaker_id
)

print(
    "Utterance number:",
    utterance_number
)


# ============================================================
# 7. Plot waveform
# ============================================================

plt.figure(
    figsize=(12, 4)
)

plt.plot(
    waveform.squeeze().numpy()
)

plt.title(
    f"Waveform - {label}"
)

plt.xlabel(
    "Sample"
)

plt.ylabel(
    "Amplitude"
)

plt.grid(
    alpha=0.3
)

plt.show()


# ============================================================
# 8. Audio settings
# ============================================================

TARGET_SAMPLE_RATE = 16000

TARGET_NUM_SAMPLES = 16000


# ============================================================
# 9. Resample function
# ============================================================

def resample_if_needed(
    waveform,
    sample_rate
):

    if sample_rate != TARGET_SAMPLE_RATE:

        resampler = torchaudio.transforms.Resample(

            orig_freq=sample_rate,

            new_freq=TARGET_SAMPLE_RATE

        )

        waveform = resampler(
            waveform
        )

    return waveform


# ============================================================
# 10. Pad or trim
# ============================================================

def pad_or_trim(
    waveform,
    target_length=16000
):

    current_length = waveform.shape[1]


    # ------------------------
    # Padding
    # ------------------------

    if current_length < target_length:

        padding_length = (
            target_length
            -
            current_length
        )

        waveform = F.pad(

            waveform,

            (
                0,
                padding_length
            )
        )


    # ------------------------
    # Trimming
    # ------------------------

    elif current_length > target_length:

        waveform = waveform[
            :,
            :target_length
        ]


    return waveform


# ============================================================
# 11. MFCC Transform
# ============================================================

mfcc_transform = torchaudio.transforms.MFCC(

    sample_rate=TARGET_SAMPLE_RATE,

    n_mfcc=13,

    melkwargs={

        "n_fft": 400,

        "hop_length": 160,

        "n_mels": 40

    }

)


# ============================================================
# 12. Test MFCC
# ============================================================

waveform = resample_if_needed(

    waveform,

    sample_rate

)


waveform = pad_or_trim(
    waveform
)


mfcc = mfcc_transform(
    waveform
)


print(
    "MFCC before transpose:",
    mfcc.shape
)
#MFCC before transpose: torch.Size([1, 13, 101])

mfcc = mfcc.squeeze(
    0
)


mfcc = mfcc.transpose(
    0,
    1
)


print(
    "MFCC for LSTM:",
    mfcc.shape
)

#MFCC for LSTM: torch.Size([101, 13])







#===================================
#===================================
#===================================
#===================================
#===================================
#===================================
#===================================
#---------for tutorials-------------
#from each class just 300 files-----
#===================================
#===================================
#===================================
#===================================
#===================================
#===================================



# ============================================================
# 13. Create a SMALL balanced subset
# ============================================================

import os
import random


random.seed(42)


# We only use this many samples from each command
MAX_SAMPLES_PER_CLASS = 300


# Store dataset indices for each class
indices_by_class = {

    command: []

    for command in COMMANDS

}


# speech_dataset._walker contains paths of WAV files
#
# Important:
# Here we DO NOT load the audio.
# We only inspect file paths.
#
# Example:
# ./data/.../yes/abc.wav
#
# folder name -> label


for index, file_path in enumerate(
    speech_dataset._walker
):

    label = os.path.basename(
        os.path.dirname(file_path)
    )


    if label in COMMANDS:

        indices_by_class[label].append(
            index
        )




for label in COMMANDS:

    print(
        label,
        len(indices_by_class[label])
    )

'''
yes 4044
no 3941
up 3723
down 3917
left 3801
right 3778
on 3845
off 3745
stop 3872
go 3880

'''



# ============================================================
# 14. Limit samples per class
# ============================================================
#juust 300 from each class

for label in COMMANDS:


    random.shuffle(
        indices_by_class[label]
    )


    indices_by_class[label] = (
        indices_by_class[label][
            :MAX_SAMPLES_PER_CLASS
        ]
    )
    
    


for label in COMMANDS:

    print(
        label,
        len(indices_by_class[label])
    )

'''
yes 300
no 300
up 300
down 300
left 300
right 300
on 300
off 300
stop 300
go 300

'''



# ============================================================
# 15. Balanced split
# ============================================================

train_indices = []

val_indices = []

test_indices = []


for label in COMMANDS:


    indices = indices_by_class[
        label
    ]


    n = len(
        indices
    )


    train_end = int(
        0.70 * n
    )


    val_end = int(
        0.85 * n
    )


    # ---------------------------
    # Train
    # ---------------------------

    train_indices.extend(

        indices[
            :train_end
        ]

    )


    # ---------------------------
    # Validation
    # ---------------------------

    val_indices.extend(

        indices[
            train_end:val_end
        ]

    )


    # ---------------------------
    # Test
    # ---------------------------

    test_indices.extend(

        indices[
            val_end:
        ]

    )









random.shuffle(
    train_indices
)

random.shuffle(
    val_indices
)

random.shuffle(
    test_indices
)





print(
    "Train:",
    len(train_indices)
)


print(
    "Validation:",
    len(val_indices)
)


print(
    "Test:",
    len(test_indices)
)

'''
Train: 2100
Validation: 450
Test: 450

'''




# ============================================================
# 16. Keyword Dataset
# ============================================================

class KeywordDataset(Dataset):


    def __init__(
        self,
        base_dataset,
        indices,
        mfcc_transform,
        label_to_index
    ):


        self.base_dataset = base_dataset

        self.indices = indices

        self.mfcc_transform = mfcc_transform

        self.label_to_index = label_to_index


    def __len__(
        self
    ):

        return len(
            self.indices
        )


    def __getitem__(
        self,
        index
    ):


        # ============================================
        # Get the real index in Speech Commands
        # ============================================

        real_index = self.indices[
            index
        ]


        # ============================================
        # Load audio using torchaudio dataset
        # ============================================

        (
            waveform,
            sample_rate,
            label,
            speaker_id,
            utterance_number

        ) = self.base_dataset[
            real_index
        ]


        # waveform:
        #
        # usually:
        # (1, number_of_samples)


        # ============================================
        # Convert stereo → mono if needed
        # ============================================

        if waveform.shape[0] > 1:

            waveform = waveform.mean(

                dim=0,

                keepdim=True

            )


        # ============================================
        # Resample if needed
        # ============================================

        waveform = resample_if_needed(

            waveform,

            sample_rate

        )


        # ============================================
        # Make every audio exactly 1 second
        # ============================================

        waveform = pad_or_trim(

            waveform,

            TARGET_NUM_SAMPLES

        )


        # Now:
        #
        # waveform.shape
        #
        # (1, 16000)


        # ============================================
        # MFCC
        # ============================================

        mfcc = self.mfcc_transform(
            waveform
        )


        # shape:
        #
        # (1, 13, 101)


        # ============================================
        # Remove channel dimension
        # ============================================

        mfcc = mfcc.squeeze(
            0
        )


        # shape:
        #
        # (13, 101)


        # ============================================
        # Prepare for LSTM
        # ============================================

        mfcc = mfcc.transpose(
            0,
            1
        )


        # shape:
        #
        # (101, 13)
        #
        # 101 timesteps
        # 13 features per timestep


        # ============================================
        # Text label → Integer
        # ============================================

        target = self.label_to_index[
            label
        ]


        target = torch.tensor(

            target,

            dtype=torch.long

        )


        return (
            mfcc,
            target
        )
    
    
    








# ============================================================
# 17. Create datasets
# ============================================================

train_dataset = KeywordDataset(

    base_dataset=speech_dataset,

    indices=train_indices,

    mfcc_transform=mfcc_transform,

    label_to_index=label_to_index

)


val_dataset = KeywordDataset(

    base_dataset=speech_dataset,

    indices=val_indices,

    mfcc_transform=mfcc_transform,

    label_to_index=label_to_index

)


test_dataset = KeywordDataset(

    base_dataset=speech_dataset,

    indices=test_indices,

    mfcc_transform=mfcc_transform,

    label_to_index=label_to_index

)






print(
    "Train Dataset:",
    len(train_dataset)
)

print(
    "Validation Dataset:",
    len(val_dataset)
)

print(
    "Test Dataset:",
    len(test_dataset)
)



'''
until now
WAV

↓ torchaudio

waveform
(1,16000)

↓ MFCC

(1,13,101)

↓ squeeze

(13,101)

↓ transpose

(101,13)

'''






# ============================================================
# 19. DataLoaders
# ============================================================

BATCH_SIZE = 32


train_loader = DataLoader(

    train_dataset,

    batch_size=BATCH_SIZE,

    shuffle=True,

    num_workers=0

)


val_loader = DataLoader(

    val_dataset,

    batch_size=BATCH_SIZE,

    shuffle=False,

    num_workers=0

)


test_loader = DataLoader(

    test_dataset,

    batch_size=BATCH_SIZE,

    shuffle=False,

    num_workers=0

)




# ============================================================
# 20. Check DataLoader shapes
# ============================================================

X_batch, y_batch = next(
    iter(train_loader)
)


print(
    "X batch:",
    X_batch.shape
)


print(
    "y batch:",
    y_batch.shape
)

'''
               X_batch

             (32,101,13)
               │   │  │
               │   │  └── 13 MFCC features
               │   │
               │   └───── 101 timesteps
               │
               └───────── 32 audio files
               
'''





# ============================================================
# 21. LSTM Model
# ============================================================

class KeywordLSTM(nn.Module):


    def __init__(
        self,
        input_size=13,
        hidden_size=128,
        num_layers=2,
        num_classes=10,
        dropout=0.2
    ):


        super().__init__()


        # ============================================
        # LSTM
        # ============================================

        self.lstm = nn.LSTM(

            input_size=input_size,

            hidden_size=hidden_size,

            num_layers=num_layers,

            batch_first=True,

            dropout=dropout

        )


        # ============================================
        # Final classifier
        # ============================================

        self.fc = nn.Linear(

            hidden_size,

            num_classes

        )


    def forward(
        self,
        x
    ):


        # ============================================
        # INPUT
        # ============================================

        # x:
        #
        # (batch, sequence, features)
        #
        # Example:
        #
        # (32, 101, 13)


        output, (
            hidden,
            cell

        ) = self.lstm(
            x
        )


        # output:
        #
        # (32, 101, 128)


        # ============================================
        # Last timestep
        # ============================================

        last_output = output[
            :,
            -1,
            :
        ]


        # shape:
        #
        # (32,128)


        # ============================================
        # Classification
        # ============================================

        logits = self.fc(
            last_output
        )


        # shape:
        #
        # (32,10)


        return logits







# ============================================================
# 22. Create model
# ============================================================

model = KeywordLSTM(

    input_size=13,

    hidden_size=64,

    num_layers=2,

    num_classes=len(COMMANDS),

    dropout=0.2

)


model = model.to(
    device
)


print(
    model
)


'''

Input
(32,101,13)

      ↓

LSTM Layer 1
13 → 64

      ↓

LSTM Layer 2
64 → 64

      ↓

output
(32,101,64)

      ↓

last timestep

(32,64)

      ↓

Linear
64 → 10

      ↓

(32,10)


'''




# ============================================================
# 23. Test model
# ============================================================

X_batch, y_batch = next(
    iter(train_loader)
)


print(
    "Input:",
    X_batch.shape
)


X_batch = X_batch.to(
    device
)


with torch.no_grad():

    logits = model(
        X_batch
    )


print(
    "Output:",
    logits.shape
)



# ============================================================
# 24. Loss + Optimizer
# ============================================================

criterion = nn.CrossEntropyLoss()


optimizer = torch.optim.Adam(

    model.parameters(),

    lr=0.001

)






# ============================================================
# 25. Training
# ============================================================

EPOCHS = 15


train_losses = []

val_losses = []

train_accuracies = []

val_accuracies = []


for epoch in range(
    EPOCHS
):


    # ========================================================
    # TRAINING
    # ========================================================

    model.train()


    total_train_loss = 0

    correct_train = 0

    total_train = 0


    for X_batch, y_batch in train_loader:


        X_batch = X_batch.to(
            device
        )


        y_batch = y_batch.to(
            device
        )


        # ------------------------------------------
        # Reset gradients
        # ------------------------------------------

        optimizer.zero_grad()


        # ------------------------------------------
        # Forward
        # ------------------------------------------

        logits = model(
            X_batch
        )


        # ------------------------------------------
        # Loss
        # ------------------------------------------

        loss = criterion(

            logits,

            y_batch

        )


        # ------------------------------------------
        # Backpropagation
        # ------------------------------------------

        loss.backward()


        # ------------------------------------------
        # Prevent exploding gradients
        # ------------------------------------------

        torch.nn.utils.clip_grad_norm_(

            model.parameters(),

            max_norm=1.0

        )


        # ------------------------------------------
        # Update weights
        # ------------------------------------------

        optimizer.step()


        total_train_loss += (
            loss.item()
        )


        # ------------------------------------------
        # Prediction
        # ------------------------------------------

        predictions = torch.argmax(

            logits,

            dim=1

        )


        correct_train += (

            predictions
            ==
            y_batch

        ).sum().item()


        total_train += (

            y_batch.size(0)

        )


    # ========================================================
    # Train metrics
    # ========================================================

    train_loss = (

        total_train_loss

        /

        len(train_loader)

    )


    train_accuracy = (

        correct_train

        /

        total_train

    )


    # ========================================================
    # VALIDATION
    # ========================================================

    model.eval()


    total_val_loss = 0

    correct_val = 0

    total_val = 0


    with torch.no_grad():


        for X_batch, y_batch in val_loader:


            X_batch = X_batch.to(
                device
            )


            y_batch = y_batch.to(
                device
            )


            logits = model(
                X_batch
            )


            loss = criterion(

                logits,

                y_batch

            )


            total_val_loss += (
                loss.item()
            )


            predictions = torch.argmax(

                logits,

                dim=1

            )


            correct_val += (

                predictions
                ==
                y_batch

            ).sum().item()


            total_val += (
                y_batch.size(0)
            )


    val_loss = (

        total_val_loss

        /

        len(val_loader)

    )


    val_accuracy = (

        correct_val

        /

        total_val

    )


    # ========================================================
    # Save history
    # ========================================================

    train_losses.append(
        train_loss
    )


    val_losses.append(
        val_loss
    )


    train_accuracies.append(
        train_accuracy
    )


    val_accuracies.append(
        val_accuracy
    )


    # ========================================================
    # Print
    # ========================================================

    print(

        f"Epoch {epoch+1:02d}/{EPOCHS}"

        f" | Train Loss: {train_loss:.4f}"

        f" | Val Loss: {val_loss:.4f}"

        f" | Train Acc: {train_accuracy*100:.2f}%"

        f" | Val Acc: {val_accuracy*100:.2f}%"

    )
    
    
'''
3 shahrivar 25 aug , 17:49




Epoch 01/15 | Train Loss: 2.2314 | Val Loss: 2.1210 | Train Acc: 15.48% | Val Acc: 21.78%
Epoch 02/15 | Train Loss: 1.9519 | Val Loss: 1.8795 | Train Acc: 28.52% | Val Acc: 33.11%
Epoch 03/15 | Train Loss: 1.7249 | Val Loss: 1.6633 | Train Acc: 38.86% | Val Acc: 43.11%
Epoch 04/15 | Train Loss: 1.5075 | Val Loss: 1.5482 | Train Acc: 46.52% | Val Acc: 50.44%
Epoch 05/15 | Train Loss: 1.3741 | Val Loss: 1.4533 | Train Acc: 51.33% | Val Acc: 52.22%
Epoch 06/15 | Train Loss: 1.2422 | Val Loss: 1.4347 | Train Acc: 56.24% | Val Acc: 55.56%
Epoch 07/15 | Train Loss: 1.1131 | Val Loss: 1.3239 | Train Acc: 61.81% | Val Acc: 61.56%
Epoch 08/15 | Train Loss: 0.9993 | Val Loss: 1.2550 | Train Acc: 67.00% | Val Acc: 58.22%
Epoch 09/15 | Train Loss: 0.8891 | Val Loss: 1.2108 | Train Acc: 70.00% | Val Acc: 60.89%
Epoch 10/15 | Train Loss: 0.7853 | Val Loss: 1.1430 | Train Acc: 73.10% | Val Acc: 66.22%
Epoch 11/15 | Train Loss: 0.7325 | Val Loss: 1.0590 | Train Acc: 75.52% | Val Acc: 68.44%
Epoch 12/15 | Train Loss: 0.6640 | Val Loss: 0.9650 | Train Acc: 77.14% | Val Acc: 72.22%
Epoch 13/15 | Train Loss: 0.5972 | Val Loss: 1.0107 | Train Acc: 80.19% | Val Acc: 67.56%
Epoch 14/15 | Train Loss: 0.5527 | Val Loss: 0.9758 | Train Acc: 82.29% | Val Acc: 70.89%
Epoch 15/15 | Train Loss: 0.5215 | Val Loss: 0.9833 | Train Acc: 82.48% | Val Acc: 72.67%





'''




# ============================================================
# 26. Plot Loss
# ============================================================

plt.figure(
    figsize=(10, 5)
)


plt.plot(
    train_losses,
    label="Train Loss"
)


plt.plot(
    val_losses,
    label="Validation Loss"
)


plt.xlabel(
    "Epoch"
)


plt.ylabel(
    "Loss"
)


plt.title(
    "Training and Validation Loss"
)


plt.legend()

plt.grid(
    alpha=0.3
)

plt.show()



# ============================================================
# 27. Plot Accuracy
# ============================================================

plt.figure(
    figsize=(10, 5)
)


plt.plot(
    train_accuracies,
    label="Train Accuracy"
)


plt.plot(
    val_accuracies,
    label="Validation Accuracy"
)


plt.xlabel(
    "Epoch"
)


plt.ylabel(
    "Accuracy"
)


plt.title(
    "Training and Validation Accuracy"
)


plt.legend()

plt.grid(
    alpha=0.3
)

plt.show()





# ============================================================
# 28. Test Evaluation
# ============================================================

model.eval()


correct = 0

total = 0


all_predictions = []

all_targets = []


with torch.no_grad():


    for X_batch, y_batch in test_loader:


        X_batch = X_batch.to(
            device
        )


        y_batch = y_batch.to(
            device
        )


        logits = model(
            X_batch
        )


        predictions = torch.argmax(

            logits,

            dim=1

        )


        correct += (

            predictions
            ==
            y_batch

        ).sum().item()


        total += (
            y_batch.size(0)
        )


        all_predictions.extend(

            predictions
            .cpu()
            .numpy()

        )


        all_targets.extend(

            y_batch
            .cpu()
            .numpy()

        )
        
     
        
test_accuracy = (
    correct
    /
    total
)


print(

    f"Test Accuracy: "
    f"{test_accuracy*100:.2f}%"

)




#Test Accuracy: 70.22%




        
        
print(

    classification_report(

        all_targets,

        all_predictions,

        target_names=COMMANDS

    )

)


#00confusion matrix
cm = confusion_matrix(

    all_targets,

    all_predictions

)


plt.figure(
    figsize=(10, 8)
)


plt.imshow(
    cm
)


plt.xticks(

    range(len(COMMANDS)),

    COMMANDS,

    rotation=45

)


plt.yticks(

    range(len(COMMANDS)),

    COMMANDS

)


plt.xlabel(
    "Predicted"
)


plt.ylabel(
    "Actual"
)


plt.title(
    "Confusion Matrix"
)


plt.colorbar()

plt.tight_layout()

plt.show()





# ============================================================
# 31. Predict one example
# ============================================================

sample_name=10


X_example, y_example = test_dataset[
    sample_name
]


print(
    "Input shape:",
    X_example.shape
)


X_example = X_example.unsqueeze(
    0
)




X_example = X_example.to(
    device
)


model.eval()


with torch.no_grad():


    logits = model(
        X_example
    )


    probabilities = torch.softmax(

        logits,

        dim=1

    )


    predicted_index = torch.argmax(

        probabilities,

        dim=1

    ).item()


    confidence = probabilities[

        0,

        predicted_index

    ].item()
    
    


actual_label = index_to_label[
    y_example.item()
]


predicted_label = index_to_label[
    predicted_index
]


print(
    "Actual:",
    actual_label
)


print(
    "Predicted:",
    predicted_label
)


print(

    f"Confidence: "
    f"{confidence*100:.2f}%"

)


'''
Input shape: torch.Size([101, 13])
Actual: right
Predicted: right
Confidence: 63.33%





'''