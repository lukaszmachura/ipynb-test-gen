IN = 'kc20_pp_pd03_nazwisko_imie.ipynb'
OUT = 'copy.ipynb'

Z1 = 44

with open(IN, 'rt') as infile:
    with open(OUT, 'wt') as outfile:
        i = 1
        for line in infile:
            if i == Z1:
                outfile.write('"$$ s=\\\\prod_{i=-4}^{13}\\\\frac{i+5}{i+1}$$\\n",\n')
            else:
                outfile.write(line)
            i += 1
