import random
from bitarray import bitarray
from tabulate import tabulate

class DescriptorBuilder:

    def generate_random(self):
        return self.make(
                bitarray(''.join(random.choice(['1', '0']) for i in range(32)), endian='big'),
                bitarray(''.join(random.choice(['1', '0']) for i in range(20)), endian='big'),
                random.choice([True, False]),
                random.choice([True, False]),
                random.choice([True, False]))


    def make(self, base_address: bitarray, limit: bitarray, readable: bool, executable: bool, writable: bool) -> bitarray:
        # big endian concept
        descriptor = bitarray()
        
        if len(base_address) != 32:
            raise ValueError("base_address must be 32 bits")
        
        if len(limit) != 20:
            raise ValueError("limit must be 20 bits")
        
        # parsing base
        base15_0 = base_address[16:32]
        base23_16 = base_address[8:16]
        base31_24 = base_address[0:8]
        
        # parsing limit
        seg_length_15_0 = limit[4:20]
        seg_length_19_16 = limit[0:4]
        
        # add base31_24
        descriptor.extend(base31_24)
        
        # create access
        AVL = bitarray('0')
        L = bitarray(''.join(random.choice(['1', '0'])), endian='big')
        D = bitarray(''.join(random.choice(['1', '0'])), endian='big')
        G = bitarray(''.join(random.choice(['1', '0'])), endian='big')

        access = bitarray()
        access.extend(G)
        access.extend(D)
        access.extend(L)
        access.extend(AVL)
        
        # add access
        descriptor.extend(access)

        # add seg_length_19_16
        descriptor.extend(seg_length_19_16)

        # create flags
        if ((not readable and executable) or (readable and executable)) and not writable:
            Type = bitarray('1')
            if readable:
                Accessibility = bitarray('1')
            else:
                Accessibility = bitarray('0')
        elif executable and writable:
            print('Note that a code segment is not writable.\nHowever, because segment base addresses can overlap, you can create a writable data segment with the same base address and limit of a code segment.')
            return None
        elif not readable and not executable and not writable:
            print('Error: Memory without attributes')
            return None
        else:  
            Type = bitarray('0')
            # Data segments are always readable
            if writable:
                Accessibility = bitarray('1')
            else:
                Accessibility = bitarray('0')
            
        Subtype = bitarray(''.join(random.choice(['1', '0'])), endian='big')
        Access = bitarray(''.join(random.choice(['1', '0'])), endian='big')
        S = bitarray(''.join(random.choice(['1', '0'])), endian='big')
        DPL = bitarray(''.join(random.choice(['1', '0']) for i in range(2)), endian='big')
        P = bitarray(''.join(random.choice(['1', '0'])), endian='big')
        
        flags = bitarray()
        flags.extend(P)
        flags.extend(DPL)
        flags.extend(S)
        flags.extend(Access)
        flags.extend(Accessibility)
        flags.extend(Subtype)
        flags.extend(Type)

        # add flags
        descriptor.extend(flags)

        # add base23_16
        descriptor.extend(base23_16)

        # add base15_0
        descriptor.extend(base15_0)

        # add seg_length_15_0
        descriptor.extend(seg_length_15_0)
        
        return descriptor

    def info(self, descriptor: bitarray) -> None:
        if descriptor is None:
            print("Make new descriptor!")
            return

        print("=== Descriptor===")
        print("Descriptor bin:", descriptor.to01())
        print("Descriptor hex:", bytearray(descriptor).hex())
        
        print("=== Base address ===")
        base31_24 = descriptor[0:8]
        base23_16 = descriptor[24:32]
        base15_0 = descriptor[32:48]

        base_address = bitarray()
        base_address.extend(base31_24)
        base_address.extend(base23_16)
        base_address.extend(base15_0)

        print("Base address bin:", base_address.to01())
        print("Base address hex:", bytearray(base_address).hex())
        
        print("=== Segment limit ===") 
        seg_length_15_0 = descriptor[48:64]
        seg_length_19_16 = descriptor[12:16]
        
        segment_limit = bitarray()
        segment_limit.extend(seg_length_19_16)
        segment_limit.extend(seg_length_15_0)
        
        print("Segment limit bin:", segment_limit.to01())
        print("Segment limit hex:", bytearray(segment_limit).hex())
        
        print("=== Access bits ===")    
        access = descriptor[8:12]
        print(tabulate({'G':str(access[0]), 'D':str(access[1]), 'L':str(access[2]), 'AVL':str(access[3])}, headers="keys", tablefmt="fancy_outline"))
        
        print("=== Flags bits ===")
        flags = descriptor[16:24]
        print(
            tabulate(
                {
                    'P':str(flags[0]), 
                    'DPL':flags[1:3].to01(), 
                    'S':str(flags[3]), 
                    'Access':str(flags[4]), 

                    'Accessibility' + 
                    '(' + 
                    ('R' if flags[7] == 0 or (flags[5] == 1 and flags[7] == 1) else '') + 
                    ('W' if flags[7] == 0 and flags[5] == 1 else '') +
                    ('X' if flags[7] == 1 else '') +
                    ')' :str(flags[5]),

                    'Subtype' +
                    '(' +
                    ('Not conforming' if flags[7] == 1 and flags[6] == 0 else '') +
                    ('Conforming' if flags[7] == 1 and flags[6] == 1 else '') +
                    ('Expand up' if flags[7] == 0 and flags[6] == 0 else '') +
                    ('Expand up' if flags[7] == 0 and flags[6] == 1 else '') +
                    ')' :str(flags[6]),

                    'Type' + 
                    '(' + 
                    ('Code' if flags[7] == 1 else 'Data') + 
                    ')' :str(flags[7])
                }, headers="keys", tablefmt="fancy_outline"))

if __name__ == "__main__":
    builder = DescriptorBuilder()
    descriptor = builder.generate_random()
    builder.info(descriptor)

   