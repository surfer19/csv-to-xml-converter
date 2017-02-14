import csv
import argparse
import pprint
import sys
#To create an option that needs no value, set the action [docs] of it to 'store_const', 'store_true' or 'store_false'.
#def useParameters():
class Main():

    def __init__(self):
        self.parser = self.init_parser()
        self.args = self.parser.parse_args()
        self.input_file = self.args.input
        self.output_file = self.args.output
        self.no_header = self.args.n
        self.root_elem = self.args.r
        print("input value = ", self.input_file)

    def init_parser(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("--input", help="write directory to your csv file")#required=True
        parser.add_argument("--output", help="write directory to save file")
        parser.add_argument("-n", help="dont generate header", action="store_true")
        parser.add_argument("-r", help="=root-element")

        return parser

        #if args.input:
        #    print("v inpute je: ", args.input)
        #    input_file = args.input
            #return  args.input
        #else:
        #    print("nic tam neni!")

    #def exportXml():
    #    f = open(path, 'w')
    #    f.write(xml_string)

    def csvToXml(self):

        with open(self.input_file, 'r') as csv_input_file:
            helper = csv.DictReader(csv_input_file)

            # for row in helper:
            #     pprint.pprint(row)

            output = '';
            #if not no_header:

            output += '<?xml version="1.0" encoding="UTF-8"?>\n'
            # iterate over all rows in file
            for row in helper:
                output += '<row>\n'
                # iterate over all columns - key is
                for key in helper.fieldnames:
                    # print(key)
                    # pprint.pprint(row)
                    # print(row.get(key))
                    output += '<'+key+'>'+ row.get(key)+'<'+key+'/>'
                output += '\n<row/>\n'

                # print(key)

            print(output)
            #path = parameter
            # export final xml
            #exportXml(output, output_file);

    #parameter = useParameters();
    #csvToXml();

mainInst = Main()
mainInst.csvToXml()
