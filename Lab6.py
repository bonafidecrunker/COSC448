# lab6q1 Dakota Joiner 300315356
from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML
import matplotlib.pyplot as plt
import numpy as np

with open('./input.txt', "r") as file:
    count = 0
    filename = './dna_lab6_count.xml'
    myList = [0, 0]
    for line in file:
        seq = line.strip('\n')
        print("Sequence: " + line[:21] + ". . . Length: " + str(len(line)))
        try:
            blast_infile = open(filename, 'r')
            print("Using saved file.")
        except:
            # perform online BLAST search if file not found and save results
            print("Performing online BLAST search")
            blastResult = NCBIWWW.qblast("blastn", 'nt', seq)
            result = blastResult.read()
            save_file = open(filename, 'w')
            save_file.write(result)
            save_file.close()
            blastResult.close()

        # fill a list with 1 if the DNA is from grapes and 0 if from fruit flies
        blast_infile = open(filename, 'r')
        blast_records = NCBIXML.parse(blast_infile)
        for rec in blast_records:
            if "Vitis vinifera" in rec.alignments[0].title:
                myList[0] += 1
            else:
                myList[1] += 1
        blast_infile.close()
        print(myList)

    # create plot showing data obtained from BLAST search
    width_of_bar = 0.35
    labels = ['Vitis vinifera', 'Drosophila melanogaster']
    x = 1
    fig, ax = plt.subplots()
    p1 = ax.bar(x-width_of_bar / 2, myList[0], width_of_bar, color='r', label='Vitis vinifera')
    p2 = ax.bar(x + width_of_bar / 2, myList[1], width_of_bar, color='b', label='Drosophila melanogaster')
    ax.set_ylabel('Count of found organisms')
    # ax.set_xticks(x, labels)
    ax.legend()
    ax.axes.xaxis.set_visible(False)
    fig.tight_layout()
    plt.show()
    plt.xticks(())

