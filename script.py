import csv
import argparse
import pprint
import sys
from contextlib import redirect_stdout

#To create an option that needs no value, set the action [docs] of it to 'store_const', 'store_true' or 'store_false'.
#def useParameters():
class Main():

    def __init__(self):
        # initialize parser
        self.parser = self.init_parser()
        self.args = self.parser.parse_args()
        self.required_together = ('i','l')
        # get values from parameters
        self.input_file = self.args.input
        self.output_file = self.args.output
        self.no_header = self.args.n
        self.root_elem = self.args.r


        # set DEFAULTS
        if (self.args.input == None):
            self.input_file = 'stdin'
        if (self.args.output == None):
            self.output_file = 'stdout'
        #if (self.args.n == None):
        #    self.no_header = 'false'


    def init_parser(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("--input", help="write directory to your csv file")#required=True
        parser.add_argument("--output", help="write directory to save file")
        parser.add_argument("-n", help="dont generate header", action="store_true")
        parser.add_argument("-r", help="=root-element")
        parser.add_argument("-i", help="=root-element")
        parser.add_argument("-l", help="=root-element")
        #parser.add_argument("-h", help="header ")


        return parser

        #if args.input:
        #    print("v inpute je: ", args.input)
        #    input_file = args.input
            #return  args.input
        #else:
        #    print("nic tam neni!")

    def export(self, xml_string):
        try:
            outFile = open(self.output_file,'w')
            outFile.write(xml_string)
            success = 1
            outFile.close()
        except IOError as err:
            success = 0
            # TODO change ret value and sys.exit ???
            sys.stderr.write('rip cant write file\n')
            exit(-99)
            #print("I/O error({0}): ".format(err))
            # problem with open or write

    def isCsvHeaderValid(input):

        if input:

            import re

            # unicode invalid characters
            RE_XML_ILLEGAL = u'([\u0000-\u0008\u000b-\u000c\u000e-\u001f\ufffe-\uffff])' + \
                             u'|' + \
                             u'([%s-%s][^%s-%s])|([^%s-%s][%s-%s])|([%s-%s]$)|(^[%s-%s])' % \
                              (chr(0xd800),chr(0xdbff),chr(0xdc00),chr(0xdfff),
                               chr(0xd800),chr(0xdbff),chr(0xdc00),chr(0xdfff),
                               chr(0xd800),chr(0xdbff),chr(0xdc00),chr(0xdfff),
                               )
            input = re.sub(RE_XML_ILLEGAL, "", input)

            # ascii control characters
            input = re.sub(r"[\x01-\x1F\x7F]", "", input)

            return input

    def csvToXml(self):
        with open(self.input_file, 'r') as csv_input_file:
            helper = csv.DictReader(csv_input_file)
            output = '';

            # SET HEADER
            if (self.no_header != True):
                output += '<?xml version="1.0" encoding="UTF-8"?>\n'
            # SET ROOT ELEMENT
            if (self.root_elem != None):
                output += '<' + self.root_elem + '>\n'

            #a = "0xd800"
            #print(Main.isCsvHeaderValid(a))

            # SET ALL ROWS
            for row in helper:
                output += '<row>\n'
                # iterate over all columns - key is
                for key in helper.fieldnames:
                    # print(key)
                    # pprint.pprint(row)
                    # print(row.get(key))
                    # print(key)

                    output += '<'+key+'>'+ row.get(key)+'<'+key+'/>'
                output += '\n<row/>\n'

            # SET END-ROOT ELEMENT
            if (self.root_elem != None):
                output += '<' + self.root_elem + '/>\n'
            #print(output)

            if (self.output_file == 'stdout'):
                sys.stdout.write(output)
            else:
                # export final xml to file
                self.export(output)

    #csvToXml();

obj = Main()
obj.csvToXml()
#obj.export()
