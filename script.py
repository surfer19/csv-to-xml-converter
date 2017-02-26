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
        #self.required_together = ('i','l')
        # get values from parameters
        self.input_file = self.args.input
        self.output_file = self.args.output
        self.no_header = self.args.n
        self.root_elem = self.args.r
        self.line_element = self.args.l
        self.header_subst = self.args.h
        self.is_index = self.args.i
        self.start_at_idx = self.args.start


        #argus = parser.parse_args(['-a'])
        #self.a = self.argus.e
        #print(a)

        #exit(0)

        if (self.args.h == None):
            self.header_subst = 'empty'


        # set DEFAULTS
        if (self.args.input == None):
            self.input_file = 'stdin'
        if (self.args.output == None):
            self.output_file = 'stdout'
        if (self.args.l == None or self.args.l == '' or self.args.l == 'is_used'):
            self.line_element = 'row'
        if (self.args.start == None or self.args.start == ''):
            self.start_at_idx = 1

        # TODO FIX
        # TODO CHANGE EXIT ERRORS

        # TODO is start_at_idx > 0 ???

        #print("self.args.l = ", self.args.l)
        #print("default = ", self.parser.get_default('l'))

        # handle -i argument
        #print("self.args.i = ", self.args.i)
        if (((self.args.l is 'is_used')) and (self.args.i is True )):
            print("exit 99")
            exit(99)

        #print("self.args.l = ", self.args.l)
        #print("default l   = ", self.parser.get_default('l'))
        #print("self.args.i = ", self.args.i)
        #print("self.start  = ", self.args.start)
        #print("self.start def= ", self.parser.get_default('start'))

        # handle --start argument
        # if one of -l or -i argument is not is_used return 30
        if ( (self.args.l is 'is_used') or (self.args.i is  False) ):
            if (self.args.start is not 'is_used'):
                print("exit 100")
                exit(100)



    def init_parser(self):
        parser = argparse.ArgumentParser('Argument helper', add_help = False)
        parser.add_argument('--help', action='help', help='show this help message and exit')
        parser.add_argument("--input", help="write directory to your csv file")#required=True
        parser.add_argument("--output", help="write directory to save file")
        parser.add_argument("-n", help="dont generate header", action="store_true")
        parser.add_argument("-r", help="=root-element")
        parser.add_argument("-h", help="string that we want replace disallowed characters", nargs='?') # action='store_true'
        parser.add_argument("-l", help="-l=line-element", nargs='?', default='is_used')
        parser.add_argument("-i", help="insert attribute index to line-element", action="store_true")
        parser.add_argument("--start", help="positive start number in i value", nargs='?', default='is_used')
        parser.add_argument("-e","--error-recovery", help="", action="store", nargs='*')

        # column element
        parser.add_argument("-c", help="=column-element")

        #parser.add_argument("-h", help="header ")
        parser.get_default('-l')

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

    # def isCsvHeaderValid(input):
    #
    #     if input:
    #
    #         import re
    #
    #         # unicode invalid characters
    #         RE_XML_ILLEGAL = u'([\u0000-\u0008\u000b-\u000c\u000e-\u001f\ufffe-\uffff])' + \
    #                          u'|' + \
    #                          u'([%s-%s][^%s-%s])|([^%s-%s][%s-%s])|([%s-%s]$)|(^[%s-%s])' % \
    #                           (chr(0xd800),chr(0xdbff),chr(0xdc00),chr(0xdfff),
    #                            chr(0xd800),chr(0xdbff),chr(0xdc00),chr(0xdfff),
    #                            chr(0xd800),chr(0xdbff),chr(0xdc00),chr(0xdfff),
    #                            )
    #         input = re.sub(RE_XML_ILLEGAL, "", input)
    #
    #         # ascii control characters
    #         input = re.sub(r"[\x01-\x1F\x7F]", "", input)
    #
    #         return input
    def isXmlValid(self):
        import xml.etree.ElementTree as ET
        tree = ET.parse(country_data.xml)
        root = tree.getroot()

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
            if (self.start_at_idx is not 'is_used'):
                idx = self.start_at_idx
                idx = int(idx)
            else:
                idx = 1
                idx = int(idx)

            # SET ALL ROWS
            for row in helper:
                # default line_element = 'row'
                output += '<' + self.line_element
                if (self.is_index):
                    output += ' index="'
                    output += str(idx)
                    output +='"'

                output += '>\n'

                # iterate over all columns - key is

                for key in helper.fieldnames:

                    if (row.get(key) is None):
                    #    if (self.args.e is True):
                            # TODO každý chybějící sloupec bude doplněn prázdným polem ??? je to ono? alebo tam nema byt ani tag??
                    #        output += '<'+key+ '></' +key+'>'
                    #    else: #err
                            print("err 32")
                            exit(32)

                    else:
                        output += '<'+key+'>'+ row.get(key)+'</'+key+'>'
                    # print(key)
                    # pprint.pprint(row)
                    # print(row.get(key))
                    # print(key)

                #default line_element = 'row'
                output += '\n</'+ self.line_element +'>\n'

            # SET END-ROOT ELEMENT
            if (self.root_elem != None):
                output += '</' + self.root_elem + '>\n'

            if (self.output_file == 'stdout'):
                sys.stdout.write(output)
            else:
                # export final xml to file
                self.export(output)

    #csvToXml();

obj = Main()
obj.csvToXml()
#obj.export()
