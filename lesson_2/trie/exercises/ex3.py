import sys
sys.path.append('src')
import trie, utils, rlp

#initialize trie from previous hash; add new [key, value] where key has common prefix
state = trie.Trie('triedb', '4a5b19d151e796482b08a1e020f1f7ef5ea7240c0171fd629598fee612892a7b'.decode('hex'))
print state.root_hash.encode('hex')
print state.root_node
print ''
state.update('\x01\x01\x02\x55', rlp.encode(['hellothere']))
print 'root hash:', state.root_hash.encode('hex')
print 'root node:', state.root_node
print 'branch node it points to:', state._decode_to_node(state.root_node[1])
print ''
state.update('\x01\x01\x02\x57', rlp.encode(['jimbojones']))
print 'root hash:', state.root_hash.encode('hex')
print 'root node:', state.root_node
branch_node = state._decode_to_node(state.root_node[1])
print 'branch node it points to:', branch_node
next_hash = branch_node[5]
print 'hash stored in branch node:', next_hash.encode('hex')
print 'branch node it points to:', state._decode_to_node(next_hash)
