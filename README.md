# QualityEstimation_WordLevel

Baseline: 22-512-256-17-output
epoch: 
20
Result from the previous epoch on dev:
F1-BAD:  0.350562830232 F1-OK:  0.911520766173
F1-score multiplied:  0.319545299605
Result from the previous epoch on test:
F1-BAD:  0.379440804651 F1-OK:  0.890474096513
F1-score multiplied:  0.337882207702
Result from the previous epoch on test:
F1-BAD:  0.379440804651 F1-OK:  0.890474096513
F1-score multiplied:  0.337882207702
[ 40537 106670  99084 ..., 465976 431894 328479]


Matern12 with pre-training

Epoch 45: \Dev set LL -0.9722672965670117, Acc 0.846903920173645, Outputs [1 1 1 ..., 1 1 1]
Result from the previous epoch on dev:
F1-BAD:  0.348111658456 F1-OK:  0.913267376174
F1-score multiplied:  0.317919020934
Epoch 45: 
Test set LL -1.1159299663805426, Acc 0.8228909969329834, Outputs [1 1 1 ..., 1 1 1]
Result from the previous epoch on test:
F1-BAD:  0.368322306705 F1-OK:  0.89700697139
F1-score multiplied:  0.330387676833
Epoch 45: 
Test set LL -1.1159299663805426, Acc 0.8228909969329834, Outputs [1 1 1 ..., 1 1 1]
Result from the previous epoch on test:
F1-BAD:  0.368322306705 F1-OK:  0.89700697139
F1-score multiplied:  0.330387676833
[  8616 406801 335128 ..., 190972 320886 532378]

RBF with pre-training

Epoch 39: \Dev set LL -0.9716229663191409, Acc 0.8514213562011719, Outputs [1 1 1 ..., 1 1 1]
Result from the previous epoch on dev:
F1-BAD:  0.335223071235 F1-OK:  0.916364312959
F1-score multiplied:  0.30718645936
Epoch 39: 
Test set LL -1.1750090773435427, Acc 0.8167999982833862, Outputs [1 1 1 ..., 1 0 1]
Result from the previous epoch on test:
F1-BAD:  0.370588794825 F1-OK:  0.892798703929
F1-score multiplied:  0.330861195711
Epoch 39: 
Test set LL -1.1750090773435427, Acc 0.8167999982833862, Outputs [1 1 1 ..., 1 0 1]
Result from the previous epoch on test:
F1-BAD:  0.370588794825 F1-OK:  0.892798703929
F1-score multiplied:  0.330861195711
[ 80053  60994 279247 ...,  16715 185116 347150]


----i found those datasets can be overfitting

baseline: 400K - 22-512-256-22-1 - total data: 413666

24                                                                                                                                                                                                         [561/1987]
Result from the previous epoch on dev:
F1-BAD:  0.386371619248 F1-OK:  0.833402206046
F1-score multiplied:  0.322002959835
Result from the previous epoch on test:
F1-BAD:  0.38033545402 F1-OK:  0.829150055812
F1-score multiplied:  0.315355162928
Result from the previous epoch on test:
F1-BAD:  0.38033545402 F1-OK:  0.829150055812
F1-score multiplied:  0.315355162928
[172341 494664   8935 ..., 529047 134712 676282]
epoch: 

best over 50

26
Result from the previous epoch on dev:
F1-BAD:  0.378638551455 F1-OK:  0.826629148814
F1-score multiplied:  0.312993663498
Result from the previous epoch on test:
F1-BAD:  0.380701352281 F1-OK:  0.827204706785
F1-score multiplied:  0.314917950486
Result from the previous epoch on test:
F1-BAD:  0.380701352281 F1-OK:  0.827204706785
F1-score multiplied:  0.314917950486
[ 58593 376708 566734 ..., 650069  35302 458851]






Epoch 29: \Dev set LL -1.6666703396440672, Acc 0.7373499870300293, Outputs [1 0 1 ..., 1 1 1]
Result from the previous epoch on dev:
F1-BAD:  0.383233532934 F1-OK:  0.833148048153
F1-score multiplied:  0.319290269951
Epoch 29: 
Test set LL -1.7019185914448822, Acc 0.7328500151634216, Outputs [1 1 1 ..., 1 0 1]
Result from the previous epoch on test:
F1-BAD:  0.3820978374 F1-OK:  0.82958568558
F1-score multiplied:  0.316982896398
Epoch 29: 
Test set LL -1.7019185914448822, Acc 0.7328500151634216, Outputs [1 1 1 ..., 1 0 1]
Result from the previous epoch on test:
F1-BAD:  0.3820978374 F1-OK:  0.82958568558
F1-score multiplied:  0.316982896398
[277392 263419 205214 ..., 318693 663928 274162]


Best from scratch - our


Epoch 31: \Dev set LL -1.5185082525091231, Acc 0.7562999725341797, Outputs [0 0 1 ..., 1 1 1]
Result from the previous epoch on dev:
F1-BAD:  0.365860005204 F1-OK:  0.84916754348
F1-score multiplied:  0.310676441877
Epoch 31: 
Test set LL -1.48930679638603, Acc 0.7612000107765198, Outputs [1 0 0 ..., 1 0 1]
Result from the previous epoch on test:
F1-BAD:  0.376338469574 F1-OK:  0.852328241915
F1-score multiplied:  0.320763906137
Epoch 31: 
Test set LL -1.48930679638603, Acc 0.7612000107765198, Outputs [1 0 0 ..., 1 0 1]
Result from the previous epoch on test:
F1-BAD:  0.376338469574 F1-OK:  0.852328241915
F1-score multiplied:  0.320763906137



Epoch 49: \Dev set LL -1.5244699696044224, Acc 0.7569500207901001, Outputs [0 1 1 ..., 1 1 1]
Result from the previous epoch on dev:
F1-BAD:  0.366314691696 F1-OK:  0.849639642426
F1-score multiplied:  0.311235483668
Epoch 49: 
Test set LL -1.4993542997521665, Acc 0.7610999941825867, Outputs [1 0 0 ..., 1 0 1]
Result from the previous epoch on test:
F1-BAD:  0.374771002355 F1-OK:  0.852339452377
F1-score multiplied:  0.319432110914
Epoch 49: 
Test set LL -1.4993542997521665, Acc 0.7610999941825867, Outputs [1 0 0 ..., 1 0 1]
Result from the previous epoch on test:
F1-BAD:  0.374771002355 F1-OK:  0.852339452377
F1-score multiplied:  0.319432110914
[69763 43104 74789 ..., 59904 15571 59948]


-- might be overfitting here.

Epoch 21: \Dev set LL -1.6866306693763533, Acc 0.734000027179718, Outputs [0 0 1 ..., 1 1 1]
Result from the previous epoch on dev:
F1-BAD:  0.387661141805 F1-OK:  0.830097087379
F1-score multiplied:  0.321796384702
Epoch 21: 
Test set LL -1.7219181280233686, Acc 0.7279000282287598, Outputs [1 1 1 ..., 1 0 1]
Result from the previous epoch on test:
F1-BAD:  0.37777269609 F1-OK:  0.825878287579
F1-score multiplied:  0.311994267341
Epoch 21: 
Test set LL -1.7219181280233686, Acc 0.7279000282287598, Outputs [1 1 1 ..., 1 0 1]
Result from the previous epoch on test:
F1-BAD:  0.37777269609 F1-OK:  0.825878287579
F1-score multiplied:  0.311994267341
[746406 108844 581472 ..., 428244 434774 411250]


200K dataset:

baseline

epoch: 
23
Result from the previous epoch on dev:
F1-BAD:  0.374941670555 F1-OK:  0.829515082092
F1-score multiplied:  0.311019770631
Result from the previous epoch on test:
F1-BAD:  0.368119266055 F1-OK:  0.823849104859
F1-score multiplied:  0.303274727821
Result from the previous epoch on test:
F1-BAD:  0.368119266055 F1-OK:  0.823849104859
F1-score multiplied:  0.303274727821
[368627  81864  22096 ..., 322831  65890 194765]
epoch: 



our:

Epoch 25: \Dev set LL -1.599708197214197, Acc 0.7480000257492065, Outputs [0 0 1 ..., 1 1 1]
Result from the previous epoch on dev:
F1-BAD:  0.378545006165 F1-OK:  0.841956726246
F1-score multiplied:  0.318718514128
Epoch 25: 
Test set LL -1.6156220276425006, Acc 0.7459999918937683, Outputs [1 1 0 ..., 1 0 1]
Result from the previous epoch on test:
F1-BAD:  0.371287128713 F1-OK:  0.840852130326
F1-score multiplied:  0.312197573141
Epoch 25: 
Test set LL -1.6156220276425006, Acc 0.7459999918937683, Outputs [1 1 0 ..., 1 0 1]
Result from the previous epoch on test:
F1-BAD:  0.371287128713 F1-OK:  0.840852130326
F1-score multiplied:  0.312197573141
[213742  80019 342918 ..., 146157 269819 208900]



---

100K

baseline:


epoch: 
19
Result from the previous epoch on dev:
F1-BAD:  0.371496116177 F1-OK:  0.82058039014
F1-score multiplied:  0.304842427948
Result from the previous epoch on test:
F1-BAD:  0.368654400355 F1-OK:  0.816127574408
F1-score multiplied:  0.300869021556
Result from the previous epoch on test:
F1-BAD:  0.368654400355 F1-OK:  0.816127574408
F1-score multiplied:  0.300869021556
[ 97785 161654  51681 ..., 117203  12221 159757]


Our:


Epoch 47: \Dev set LL -1.5825896184602455, Acc 0.7505499720573425, Outputs [1 0 1 ..., 1 1 1]
Result from the previous epoch on dev:
F1-BAD:  0.369996211643 F1-OK:  0.844487391291
F1-score multiplied:  0.312457135558
Epoch 47: 
Test set LL -1.5882147785229073, Acc 0.7494500279426575, Outputs [1 1 1 ..., 1 0 1]
Result from the previous epoch on test:
F1-BAD:  0.376973766008 F1-OK:  0.843195544012
F1-score multiplied:  0.317862599707
Epoch 47: 
Test set LL -1.5882147785229073, Acc 0.7494500279426575, Outputs [1 1 1 ..., 1 0 1]
Result from the previous epoch on test:
F1-BAD:  0.376973766008 F1-OK:  0.843195544012
F1-score multiplied:  0.317862599707
[160097  39868  71128 ...,  62220 102373  37137]


----
50K

Baseline:

epoch: 
28
Result from the previous epoch on dev:
F1-BAD:  0.355314588324 F1-OK:  0.84056253703
F1-score multiplied:  0.298664131805
Result from the previous epoch on test:
F1-BAD:  0.35825739608 F1-OK:  0.839288505424
F1-score multiplied:  0.300681314513
Result from the previous epoch on test:
F1-BAD:  0.35825739608 F1-OK:  0.839288505424
F1-score multiplied:  0.300681314513
[ 9745 91873 60055 ..., 75372 46558 24940]
epoch: 


baseline with 50-iterations


epoch: 
32
Result from the previous epoch on dev:
F1-BAD:  0.360072798544 F1-OK:  0.860882003835
F1-score multiplied:  0.309980192337
Result from the previous epoch on test:
F1-BAD:  0.36046349295 F1-OK:  0.860492736852
F1-score multiplied:  0.310176217584
Result from the previous epoch on test:
F1-BAD:  0.36046349295 F1-OK:  0.860492736852
F1-score multiplied:  0.310176217584
[90710 83938 59820 ..., 66852 33449 80149]




Our system:

Epoch 2: \Dev set LL -0.577487081833119, Acc 0.7189000248908997, Outputs [0 0 1 ..., 1 1 1]
Result from the previous epoch on dev:
F1-BAD:  0.366178128523 F1-OK:  0.819402505622
F1-score multiplied:  0.300047276016
Epoch 2: 
Test set LL -0.5784063522864644, Acc 0.7174000144004822, Outputs [1 0 0 ..., 1 0 1]
Result from the previous epoch on test:
F1-BAD:  0.362939585212 F1-OK:  0.818427139553
F1-score multiplied:  0.297039606555
Epoch 2: 
Test set LL -0.5784063522864644, Acc 0.7174000144004822, Outputs [1 0 0 ..., 1 0 1]
Result from the previous epoch on test:
F1-BAD:  0.362939585212 F1-OK:  0.818427139553
F1-score multiplied:  0.297039606555
[65019 52601 13891 ..., 91050 69501 85684]


Our System from scratch:

Epoch 44: \Dev set LL -1.4502707160353072, Acc 0.7684500217437744, Outputs [0 0 1 ..., 1 1 1]
Result from the previous epoch on dev:
F1-BAD:  0.366917293233 F1-OK:  0.858314211412
F1-score multiplied:  0.314930327195
Epoch 44: 
Test set LL -1.4299545790156774, Acc 0.770799994468689, Outputs [1 0 0 ..., 1 0 1]
Result from the previous epoch on test:
F1-BAD:  0.372398685652 F1-OK:  0.859799363837
F1-score multiplied:  0.320188153017
Epoch 44: 
Test set LL -1.4299545790156774, Acc 0.770799994468689, Outputs [1 0 0 ..., 1 0 1]
Result from the previous epoch on test:
F1-BAD:  0.372398685652 F1-OK:  0.859799363837
F1-score multiplied:  0.320188153017
[14778  2137 90965 ..., 64635 39911 91933]


