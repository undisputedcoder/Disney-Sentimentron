# Disney Sentimentron

A web app which classifies the sentiment of Disneyland review(s). The user review is sent as input to a pre-trained model that returns an output describing the sentiment as either **positive** or **negative**.

The [Disneyland-Reviews]((https://www.kaggle.com/datasets/arushchillar/disneyland-reviews)) dataset was used for training the model. The model itself is very basic consisting of an input layer, an embedding layer, 1D global average pooling layer and a dense layer as the output layer. The model was compiled using the binary crossentropy loss function and adam optimizer.

## How to run

Install the libraries and run with streamlit.

```
pip install -r requirements.txt
streamlit run nlp.py
```

*The app will open with the default web browser*

<a data-flickr-embed="true" href="https://www.flickr.com/photos/194810959@N06/52202927005/in/dateposted-public/" title="screely-1657293974839"><img src="https://live.staticflickr.com/65535/52202927005_eec0c22306_c.jpg" width="800" height="418" alt="screely-1657293974839"></a><script async src="//embedr.flickr.com/assets/client-code.js" charset="utf-8"></script>

## Tasks
- [ ] Add jupyter notebook