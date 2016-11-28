Accompanying code for blog post: [Recurring Neural Networks and Star Trek](https://simonb83.github.io/rnns-star-trek.html).

__Data__

Data source: http://www.st-minutiae.com/resources/scripts/#thenextgeneration

Once zip file has been downloaded an unzipped, to combine all scripts into a single file:

`python combine_scripts.py`

__Markov Chain Models__

For finding character or n-gram pairs based on training text:

`python markov_train.py`

Flags:
- -f, Path to file containing training data
- -l, Number of characters to use, i.e. 1 = single characters, 2 = bi-grams etc.

Outputs dictionary of pairs to json file, with:

key = character n-gram<br />
value = list of n-grams


For generating new text:

`python markov_generate.py`

Flags:
- -f, Path to file containing transition frequencies
- -s, Optional seed for getting started
- -l, Output length, number of characters

__RNN Models__

To install the Torch library:

`git clone https://github.com/jcjohnson/torch-rnn`

Instruction for use along with available options are described in detail on the github page.

_Training Params Used:_

Attempt 1:

th train.lua -input_h5 data/star_trek.h5 -input_json data/star_trek.json \
-model_type rnn -num_layers 2 -rnn_size 128 \
-seq_length 100 -lr_decay_every 10 \
-lr_decay_factor 0.95

Attempt 2:

th train.lua -input_h5 data/star_trek.h5 -input_json data/star_trek.json \
-model_type lstm -num_layers 2 -rnn_size 128 \
-seq_length 100 -lr_decay_every 10 \
-lr_decay_factor 0.95

Attempt 3:

th train.lua -input_h5 data/star_trek.h5 -input_json data/star_trek.json 
-model_type lstm -num_layers 3

Attempt 4:

th train.lua -input_h5 data/star_trek.h5 -input_json data/star_trek.json \
-seq_length 200 -rnn_size 256 \
-model_type lstm -num_layers 3


Output log files are in `Logs/`

iPython Notebook for visualizing training curves: [Learning_vis.ipynb](Learning_vis.ipynb)

_Text Generation_

Examples of generated text are in `Results/`, based on the following flags:

<table>
    <tr>
        <th>File Name</th>
        <th>Temperature</th>
        <th>Seed</th>
    </tr>
    <tr>
        <td>Sample.txt</td>
        <td>1</td>
        <td>None</td>
    </tr>
    <tr>
        <td>Sample2.txt</td>
        <td>0</td>
        <td>None</td>
    </tr>
    <tr>
        <td>Sample3.txt</td>
        <td>0.5</td>
        <td>None</td>
    </tr>
    <tr>
        <td>Sample4.txt</td>
        <td>0.7</td>
        <td>None</td>
    </tr>
    <tr>
        <td>Sample5.txt</td>
        <td>0.8</td>
        <td>None</td>
    </tr>
    <tr>
        <td>Sample6.txt</td>
        <td>0.25</td>
        <td>None</td>
    </tr>
    <tr>
        <td>Sample7.txt</td>
        <td>1</td>
        <td>"Captain"</td>
    </tr>
    <tr>
        <td>Sample8.txt</td>
        <td>0.8</td>
        <td>"1  INT. MAIN BRIDGE"</td>
    </tr>
    <tr>
        <td>Sample10.txt</td>
        <td>0.7</td>
        <td>Paramount</td>
    </tr>
    <tr>
        <td>Sample11.txt</td>
        <td>0.1</td>
        <td>None</td>
    </tr>
    <tr>
        <td>Sample13.txt</td>
        <td>0.75</td>
        <td>None</td>
    </tr>
</table>
