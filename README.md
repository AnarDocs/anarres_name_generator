Generator for Pravic genderneutral names 
========================================

On Anarres, the planet inhabited by anarchists, in the great ambiguous utopia by Ursula K. Le Guin, every human gets a random computer generated name. This name is unique during lifetime and thus can be used to identify. They use only these names, no id-numbers, no titles and no hints on gender.

Zrajm C Akfohg did an awesome analysis http://zrajm.org/nerd/pravic/ of the name patterns and the amount of possible names. I adopted the algorithm a version similar to the one without extrapolation described there.

The web script can be placed in a web accessable path & called via -

http://PATH/pravic_names.html

Refresh the page to get a new name.

The Python version can be called by -

> python3 pravic_names.py

The script can be called by -

> ruby namesGenerator.rb

[On the Ruby & Python versions] It generates 10 names for each run. 
