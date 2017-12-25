#import BlockChain
import Block
import BlockParams


def create_block(index, previous_hash, timestamp, data):
    params = BlockParams.BlockParams(index, previous_hash, timestamp, data)
    return Block.Block(params)

def main():
    prev_block = create_block(0, '0', 1, 'first_block')

    new_block = create_block(1, '0', 1, 'second block')
    print new_block.has_valid_index(prev_block)

    new_block = create_block(2, '0', 1, 'second block')
    print new_block.has_valid_index(prev_block)

    prev_block = create_block(0, '0', 1, 'first_block')
    prev_hash = prev_block.hash
    new_block = create_block(1, prev_hash, 1, 'second block')
    print new_block.has_valid_previous_hash(prev_block)

    new_block = create_block(2, '0', 1, 'second_block')
    print new_block.has_valid_previous_hash(prev_block)

    new_block = create_block(2, '0', 1, 'second_block')
    print new_block.has_valid_hash()


if __name__ == '__main__':
    main()