#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 04:51:52 2026

@author: apm
"""

'''

(base) apm@APMs-MacBook-Pro Python140505-Py07 % python3 -c "import sys; print(sys.path)"
['', '/Users/apm/anaconda3/lib/python312.zip', '/Users/apm/anaconda3/lib/python3.12', '/Users/apm/anaconda3/lib/python3.12/lib-dynload', '/Users/apm/anaconda3/lib/python3.12/site-packages']


(base) apm@APMs-MacBook-Pro Python140505-Py07 % ls /Users/apm/anaconda3/lib/python3.12
LICENSE.txt
__future__.py
__hello__.py
__phello__
__pycache__
_aix_support.py
_collections_abc.py
_compat_pickle.py
_compression.py
_markupbase.py

....

.....

zipfile
zipimport.py
zoneinfo


'''


import os


python_path = "/Users/apm/anaconda3/lib/python3.12"


python_files = []


for root, dirs, files in os.walk(python_path):

    for file in files:

        if file.endswith(".py"):

            full_path = os.path.join(
                root,
                file
            )

            python_files.append(
                full_path
            )


print(
    "Number of Python files:",
    len(python_files)
)


for file in python_files[:50]:

    print(file)
    
    




import os


python_path = "/Users/apm/anaconda3/lib/python3.12"

output_file = "python_code_corpus.txt"


count = 0


with open(
    output_file,
    "w",
    encoding="utf-8"
) as out:


    for root, dirs, files in os.walk(python_path):


        for file in files:


            if file.endswith(".py"):


                file_path = os.path.join(
                    root,
                    file
                )


                try:

                    with open(
                        file_path,
                        "r",
                        encoding="utf-8"
                    ) as f:

                        code = f.read()


                    out.write(
                        "\n\n"
                    )

                    out.write(
                        "# FILE: "
                        + file_path
                        + "\n"
                    )

                    out.write(
                        code
                    )


                    count += 1


                except Exception:

                    pass



print(
    "Python files collected:",
    count
)


print(
    "Saved:",
    output_file
)
    
'''
Python files collected: 31102
Saved: python_code_corpus.txt

'''

#-----but it was too much and rare characters-----
#==================================================
#==================================================
#==================================================

import os
import re


python_path = "/Users/apm/anaconda3/lib/python3.12"


output_file = "python_code_corpus_clean.txt"


# ----------------------------------------
# Modules we want
# ----------------------------------------

allowed_modules = [

    "asyncio",
    "collections",
    "concurrent",
    "json",
    "logging",
    "urllib",

]


allowed_files = [

    "datetime.py",
    "functools.py",
    "itertools.py",
    "pathlib.py",
    "random.py",
    "re.py",
    "statistics.py",
    "string.py",
    "typing.py",

]


# ----------------------------------------
# Check if file is good
# ----------------------------------------

def is_good_python_file(path):


    filename = os.path.basename(path)


    # ignore tests
    if "test" in path.lower():
        return False


    # ignore cache
    if "__pycache__" in path:
        return False


    # ignore pyd files
    if filename.endswith(".pyi"):
        return False


    # size filter
    size = os.path.getsize(path)

    if size < 1000:
        return False


    return True



# ----------------------------------------
# Check text quality
# ----------------------------------------

def clean_code_quality(text):


    # Count non-ascii chars

    non_ascii = sum(
        1
        for c in text
        if ord(c) > 127
    )


    ratio = non_ascii / max(
        len(text),
        1
    )


    # If too many strange chars reject

    if ratio > 0.05:
        return False


    return True



# ----------------------------------------
# Collect files
# ----------------------------------------

selected_files = []


for root, dirs, files in os.walk(
    python_path
):


    for file in files:


        full_path = os.path.join(
            root,
            file
        )


        if not file.endswith(".py"):
            continue


        relative = os.path.relpath(
            full_path,
            python_path
        )


        module_name = relative.split(
            os.sep
        )[0]


        take = False


        if module_name in allowed_modules:
            take = True


        if file in allowed_files:
            take = True


        if take and is_good_python_file(full_path):

            selected_files.append(
                full_path
            )



print(
    "Selected files:",
    len(selected_files)
)


for f in selected_files[:30]:
    print(f)


'''
Selected files: 87
/Users/apm/anaconda3/lib/python3.12/functools.py
/Users/apm/anaconda3/lib/python3.12/random.py
/Users/apm/anaconda3/lib/python3.12/statistics.py
/Users/apm/anaconda3/lib/python3.12/string.py
/Users/apm/anaconda3/lib/python3.12/typing.py
/Users/apm/anaconda3/lib/python3.12/pathlib.py
/Users/apm/anaconda3/lib/python3.12/urllib/error.py
/Users/apm/anaconda3/lib/python3.12/urllib/request.py
/Users/apm/anaconda3/lib/python3.12/urllib/response.py
/Users/apm/anaconda3/lib/python3.12/urllib/robotparser.py
/Users/apm/anaconda3/lib/python3.12/urllib/parse.py
/Users/apm/anaconda3/lib/python3.12/site-packages/astroid/typing.py
/Users/apm/anaconda3/lib/python3.12/site-packages/flask/typing.py
/Users/apm/anaconda3/lib/python3.12/site-packages/pylint/typing.py
/Users/apm/anaconda3/lib/python3.12/site-packages/pylint/extensions/typing.py
/Users/apm/anaconda3/lib/python3.12/site-packages/sympy/core/random.py
/Users/apm/anaconda3/lib/python3.12/site-packages/flake8/statistics.py
/Users/apm/anaconda3/lib/python3.12/site-packages/redis/typing.py
/Users/apm/anaconda3/lib/python3.12/site-packages/seaborn/_core/typing.py
/Users/apm/anaconda3/lib/python3.12/site-packages/pymatgen/util/string.py
/Users/apm/anaconda3/lib/python3.12/site-packages/pymatgen/util/typing.py
/Users/apm/anaconda3/lib/python3.12/site-packages/referencing/typing.py
/Users/apm/anaconda3/lib/python3.12/site-packages/jedi/inference/gradual/typing.py
/Users/apm/anaconda3/lib/python3.12/site-packages/websockets/typing.py
/Users/apm/anaconda3/lib/python3.12/site-packages/sqlalchemy/util/typing.py
/Users/apm/anaconda3/lib/python3.12/site-packages/emmet/core/types/typing.py
/Users/apm/anaconda3/lib/python3.12/site-packages/sklearn/utils/random.py
/Users/apm/anaconda3/lib/python3.12/site-packages/monty/functools.py
/Users/apm/anaconda3/lib/python3.12/site-packages/monty/string.py
/Users/apm/anaconda3/lib/python3.12/site-packages/monty/re.py

'''
# ----------------------------------------
# Create corpus
# ----------------------------------------

count = 0


with open(
    output_file,
    "w",
    encoding="utf-8"
) as out:


    for file_path in selected_files:


        try:

            with open(
                file_path,
                "r",
                encoding="utf-8"
            ) as f:

                code = f.read()



            if not clean_code_quality(code):
                continue



            out.write(
                "\n\n"
            )


            out.write(
                "# FILE: "
                + file_path
                + "\n\n"
            )


            out.write(
                code
            )


            count += 1



        except Exception as e:

            print(
                "Skip:",
                file_path,
                e
            )



print(
    "\nFinal files:",
    count
)


print(
    "Saved:",
    output_file
)






import numpy as np
import re
import json
import torch

with open(
    "python_code_corpus_clean.txt",
    "r",
    encoding="utf-8"
) as f:

    code_text = f.read()


print(
    "Total characters:",
    len(code_text)
)


print(
    code_text[:1000]
)



#just very high spaces
def clean_code(text):

    # remove too many empty lines
    text = re.sub(
        r"\n\s*\n\s*\n+",
        "\n\n",
        text
    )


    # remove trailing spaces
    lines = []

    for line in text.split("\n"):

        lines.append(
            line.rstrip()
        )


    text = "\n".join(
        lines
    )


    return text

code_text = clean_code(
    code_text
)


#************************
#************************
#************************
code_text = clean_code(
    code_text[:200000]
)



characters = sorted(
    list(
        set(code_text)
    )
)


VOCAB_SIZE = len(
    characters
)


print(
    "Vocabulary size:",
    VOCAB_SIZE
)


print(
    characters
)

'''
Vocabulary size: 99
['\n', ' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', '\\', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~', 'ö', 'Ł', '–']

'''


#char to id
char_to_idx = {

    char: idx

    for idx, char
    in enumerate(characters)

}

idx_to_char = {

    idx: char

    for char, idx
    in char_to_idx.items()

}




#encode all
encoded_code = np.array(

    [
        char_to_idx[c]
        for c in code_text
    ],

    dtype=np.int64
)


SEQUENCE_LENGTH = 100


def create_sequences(
    data,
    seq_length
):

    X = []
    y = []


    for i in range(
        len(data)-seq_length
    ):


        X.append(
            data[
                i:i+seq_length
            ]
        )


        y.append(
            data[
                i+seq_length
            ]
        )


    return (
        np.array(X),
        np.array(y)
    )

X, y = create_sequences(
    encoded_code,
    SEQUENCE_LENGTH
)


#-----see one real input
sample_id = 100
input_ids = X[sample_id]
input_text = "".join(

    idx_to_char[i]

    for i in input_ids

)
target_char = idx_to_char[
    y[sample_id]
]
print(
    "INPUT:"
)

print(
    input_text
)


print(
    "\nTARGET:"
)

print(
    target_char
)


#--------pytorch


from torch.utils.data import (
    TensorDataset,
    DataLoader
)


import torch
import torch.nn as nn

from torch.utils.data import (
    TensorDataset,
    DataLoader
)

import matplotlib.pyplot as plt


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


print(device)



X_tensor = torch.tensor(
    X,
    dtype=torch.long
)


y_tensor = torch.tensor(
    y,
    dtype=torch.long
)




dataset = TensorDataset(
    X_tensor,
    y_tensor
)

BATCH_SIZE = 64



train_loader = DataLoader(
    dataset,
    batch_size=BATCH_SIZE,
    shuffle=True
)


class PythonAutocompleteLSTM(nn.Module):

    def __init__(
        self,
        vocab_size,
        embedding_dim=128,
        hidden_size=256,
        num_layers=2,
        dropout=0.2
    ):

        super().__init__()


        # -----------------------------
        # Character embedding
        # -----------------------------

        self.embedding = nn.Embedding(
            vocab_size,
            embedding_dim
        )


        # -----------------------------
        # LSTM
        # -----------------------------

        self.lstm = nn.LSTM(

            input_size=embedding_dim,

            hidden_size=hidden_size,

            num_layers=num_layers,

            batch_first=True,

            dropout=dropout
        )


        # -----------------------------
        # Classifier
        # -----------------------------

        self.fc = nn.Linear(

            hidden_size,

            vocab_size

        )


    def forward(
        self,
        x
    ):


        # x:
        #
        # (batch, sequence)
        #
        # (64,100)


        embedded = self.embedding(
            x
        )


        # embedded:
        #
        # (64,100,128)


        output, (
            hidden,
            cell
        ) = self.lstm(
            embedded
        )


        # output:
        #
        # (64,100,256)


        # Take last timestep

        last_hidden = output[
            :,
            -1,
            :
        ]


        # (64,256)


        logits = self.fc(
            last_hidden
        )


        # (64,vocab_size)


        return logits
    
    
VOCAB_SIZE = len(char_to_idx)

print(
    VOCAB_SIZE
)

model = PythonAutocompleteLSTM(

    vocab_size=VOCAB_SIZE,

    embedding_dim=16,

    hidden_size=64,

    num_layers=2,

    dropout=0.2

)

model = model.to(device)

print(model)

criterion = nn.CrossEntropyLoss()

optimizer = torch.optim.Adam(

    model.parameters(),

    lr=0.01

)


EPOCHS = 10


train_losses = []


for epoch in range(EPOCHS):


    model.train()


    total_loss = 0


    for X_batch, y_batch in train_loader:


        X_batch = X_batch.to(device)

        y_batch = y_batch.to(device)



        # Forward

        logits = model(
            X_batch
        )


        # Loss

        loss = criterion(
            logits,
            y_batch
        )


        # Reset gradients

        optimizer.zero_grad()


        # Backprop

        loss.backward()


        # Prevent exploding gradient

        torch.nn.utils.clip_grad_norm_(

            model.parameters(),

            max_norm=1.0

        )


        # Update

        optimizer.step()


        total_loss += loss.item()



    epoch_loss = (
        total_loss
        /
        len(train_loader)
    )


    train_losses.append(
        epoch_loss
    )


    print(

        f"Epoch {epoch+1}/{EPOCHS}"

        f" | Loss: {epoch_loss:.4f}"

    )



'''
with 
    embedding_dim=16,

    hidden_size=64,

    num_layers=2,

    dropout=0.2
    
    
    
    





'''


#-----Plot------
plt.figure(figsize=(10,5))

plt.plot(
    train_losses
)

plt.xlabel(
    "Epoch"
)

plt.ylabel(
    "Loss"
)

plt.title(
    "Python Autocomplete LSTM Training"
)

plt.grid()

plt.show()











def encode_text(
    text,
    char_to_idx
):

    encoded = []

    for ch in text:

        encoded.append(
            char_to_idx[ch]
        )


    return encoded


def decode_ids(
    ids,
    idx_to_char
):

    text = ""

    for idx in ids:

        text += idx_to_char[idx]


    return text


def generate_code(
    model,
    seed_text,
    char_to_idx,
    idx_to_char,
    sequence_length,
    device,
    generation_length=200
):

    model.eval()


    generated = seed_text


    for _ in range(
        generation_length
    ):


        # --------------------------------
        # فقط آخرین sequence_length
        # کاراکترها
        # --------------------------------

        input_text = generated[
            -sequence_length:
        ]


        # --------------------------------
        # تبدیل char به id
        # --------------------------------

        encoded = encode_text(
            input_text,
            char_to_idx
        )


        # tensor

        x = torch.tensor(

            encoded,

            dtype=torch.long

        )


        x = x.unsqueeze(0)


        # shape:
        #
        # (1, sequence_length)


        x = x.to(device)



        # --------------------------------
        # Prediction
        # --------------------------------

        with torch.no_grad():

            logits = model(
                x
            )


        # shape:
        #
        # (1, vocab_size)


        logits = logits[0]


        # --------------------------------
        # انتخاب بیشترین احتمال
        # --------------------------------

        next_id = torch.argmax(
            logits
        ).item()



        next_char = idx_to_char[
            next_id
        ]


        generated += next_char



    return generated





seed = "for i in "


seed = """
def calculate_sum
"""

result = generate_code(

    model,

    seed,

    char_to_idx,

    idx_to_char,

    sequence_length=100,

    device=device,

    generation_length=400
)


print(result)






#-----advanced geenrators------
def generate_code(
    model,
    seed_text,
    char_to_idx,
    idx_to_char,
    sequence_length,
    device,
    generation_length=200,
    temperature=0.8
):


    model.eval()


    generated = seed_text



    for _ in range(
        generation_length
    ):



        input_text = generated[
            -sequence_length:
        ]


        encoded = encode_text(
            input_text,
            char_to_idx
        )


        x = torch.tensor(
            encoded,
            dtype=torch.long
        )


        x = x.unsqueeze(0)

        x = x.to(device)



        with torch.no_grad():

            logits = model(
                x
            )



        logits = logits[0]



        # Temperature

        logits = (
            logits
            /
            temperature
        )



        probabilities = torch.softmax(
            logits,
            dim=0
        )



        # Sampling

        next_id = torch.multinomial(

            probabilities,

            num_samples=1

        ).item()



        next_char = idx_to_char[
            next_id
        ]


        generated += next_char



    return generated



seed = "def _deduplicate(params)"
output = generate_code(

    model,

    seed,

    char_to_idx,

    idx_to_char,

    100,

    device,

    generation_length=200,

    temperature=0.5

)
print(output)
