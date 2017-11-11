#! /usr/bin/env pythonA

import re

class caesar:
    def __init__( self ):
        pass

    def crypt( self, **arg ):
        if not arg.has_key('orig') or not isinstance( arg['orig'],str ):
            raise Exception( 'no original data!' )

        """
        p = re.compile( '^[A-Za-z]+$' )
        if p.match( arg['orig'] ) == None:
            raise Exception( 'Original data format is illegal! Must be all alphabet!' )
        """

        min_chr_lower = ord( 'a' )
        max_chr_lower = ord( 'z' )
        min_chr_upper = ord( 'A' )
        max_chr_upper = ord( 'Z' )

        scope_len = max_chr_lower - min_chr_lower + 1

        if arg.has_key( 'offset' ):
            if not isinstance( arg['offset'],int ):
                raise Exception( 'offset data is illegal!' )

            if arg['offset']%scope_len == 0:
                return arg['orig']
            else:
                curr_offset = arg['offset']%scope_len

            tmp_list = list()
            for i in arg['orig']:
                if ord(i)>max_chr_lower or ord(i)<min_chr_upper:
                    tmp_list.append( i )
                    continue

                if ord(i)>max_chr_upper and ord(i)<min_chr_lower:
                    tmp_list.append( i )
                    continue

                curr_max_chr = max_chr_lower
                curr_min_chr = min_chr_lower

                if ord(i)<=max_chr_upper:
                    curr_max_chr = max_chr_upper
                    curr_min_chr = min_chr_upper

                if ord(i)+curr_offset > curr_max_chr:
                    tmp_list.append( chr(ord(i)+curr_offset-curr_max_chr+curr_min_chr-1) )
                else:
                    tmp_list.append( chr(ord(i)+curr_offset) )

            return ''.join( tmp_list )
        else:
            crypt_data = dict()
            for i in range(scope_len-1):
                crypt_data[i+1] = self.crypt( orig=arg['orig'], offset=i+1 )
            return crypt_data

class fence:
    orig_data = ''
    def_groups = 2

    def __init__( self, orig_data ):
        self.orig_data = orig_data

    def crypt( self, **arg ):
        groups = self.def_groups

        if arg.has_key( 'groups' ) and isinstance( arg['groups'],int ) and len(self.orig_data)>arg['groups']:
            groups = arg['groups']

        tmp_data = dict()
        for i in range(groups):
            segment_len = len(self.orig_data)/groups
            if len(self.orig_data)%groups > 0:
                segment_len += 1

            if segment_len*(i+1) < len(self.orig_data ):
                tmp_data[i] = self.orig_data[segment_len*i:segment_len*(i+1)]
            else:
                tmp_data[i] = self.orig_data[segment_len*i:]


        encrypt_data = ''
        for i in range(segment_len):
            for j in range(groups):
                if len(tmp_data[j]) >= i+1:
                    encrypt_data += tmp_data[j][i]

        return encrypt_data

    def decrypt( self, **arg ):
        pass

class morse:
    plain_data  = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890.:,;?='/!-_\"()$&@"
    cipher_data = '.- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --.. .---- ..--- ...-- ....- ..... -.... --... ---.. ----. ----- .-.-.- ---... --..-- -.-.-. ..--.. -...- .----. -..-. -.-.-- -....- ..--.- .-..-. -.--. -.--.- ...-..- .-... .--.-.'

    def __init__( self,orig_data ):
        self.orig_data = orig_data
        self.cipher_list = self.cipher_data.split()

    def encode( self ):
        res_str = ''
        tmp_cnt = 0
        for i in self.orig_data:
            if i.upper() in self.plain_data:
                if tmp_cnt > 0:
                    res_str += ' '
                res_str += self.cipher_list[self.plain_data.index(i.upper())]
                tmp_cnt += 1
            else:
                res_str += i
        return res_str

    def decode( self ):
        res_str = ''
        orig_list = self.orig_data.split()

        import re
        p = re.compile( '[-.]+' )

        for i in orig_list:
            m = p.search( i )
            if m != None:
                c_data = i[m.span()[0]:m.span()[1]]

                if m.span()[0] > 0:
                    res_str += i[:m.span()[0]]
                res_str += self.plain_data[self.cipher_list.index(c_data)]
                if m.span()[1] < len(i):
                    res_str += i[m.span()[1]:]
            else:
                res_str += i
        return res_str
