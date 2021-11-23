class Rank2TaxPlugin:
    def input(self, infile):
        self.myfile = open(infile, 'r')
        self.firstline = self.myfile.readline()
    def run(self):
        self.firstline = self.firstline.replace("Rank1","Kingdom")
        self.firstline = self.firstline.replace("Rank2","Phylum")
        self.firstline = self.firstline.replace("Rank3","Class")
        self.firstline = self.firstline.replace("Rank4","Order")
        self.firstline = self.firstline.replace("Rank5","Family")
        self.firstline = self.firstline.replace("Rank6","Genus")
        self.firstline = self.firstline.replace("Rank7","Species")

    def output(self, outfile):
        outputfile = open(outfile, 'w')
        outputfile.write(self.firstline)
        for line in self.myfile:
            outputfile.write(line)
