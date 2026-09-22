// children [i] means current letter
class TrieNode {
   public:
    bool ending;
    TrieNode* children[26];

    TrieNode() {
        for (int i = 0; i < 26; i++) {
            children[i] = nullptr;
        }
        ending = false;
    }
    void insert(char val) {
        if (this->children[val - 'a'] == nullptr) {
            this->children[val - 'a'] = new TrieNode();
        }
    }

    TrieNode* search(char val) { return this->children[val - 'a']; }
};

class PrefixTree {
   public:
    TrieNode* root;
    PrefixTree() { this->root = new TrieNode(); }

    void insert(string word) {
        TrieNode* head = root;
        for (char i : word) {
            head->insert(i);
            head = head->search(i);
        }
        head->ending = true;
    }

    bool search(string word) {
        TrieNode* head = root;
        for (auto i : word) {
            head = head->search(i);
            if (head == nullptr) {
                return false;
            }
        }
        return head->ending ? true : false;
    }

    bool startsWith(string prefix) {
        TrieNode* head = root;
        for (auto i : prefix) {
            head = head->search(i);
            if (head == nullptr) {
                return false;
            }
        }
        return true;
    }
};
