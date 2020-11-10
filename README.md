# CS229-FinalProject


### TODOs:
1. Save Youtube Files to path - local computer
2. Parse to similar path, but in matrix form
  - ideally we dont to want to save full youtube videos on local
  - chop full game into chunks of 30 secs
   - assumption: with these chunks, there will be some sort of highlight in it

### Milestone Model:
- 1 3-D CNN layer - "3DConv" (keras)
  - input videos -> probability of chopped parts being a highlight
- Hand-label 2 full games each 3*2 = 6 matches
 1. chop full video into 30 second segments
 - Parsing.py

 - for each 30-sec-segment:
  - if this segment is in the highlight video
    - label as 1
  - else
    - label as 0

  2. Make csv file for each match as below:
  index | x | y
  0 | matrix(30s) | {0,1}
  compare cached highlight frame with frame from full videos frame in highlight_frames


### After milestone:
1. Figure out if we can have cloud storage?

## Files:
- Parsing.py: downloads full-length youtube videos, parses it into 30 second segments
- TrainSupervisedModel.py: loads labeled, training data and trains on model

## Hyperparameters:
- length of segment
## Brainstorm:
- Unsupervised
  - may be easier because we only need positive examples

- Supervised
  - train on pictures rather than videos - overcomes problem of how big "chunks" are
  - how do we label or classify?

- Parsing
 - set of 3D matrices - if we have seen, is a highlight
 - pure highlight frames
