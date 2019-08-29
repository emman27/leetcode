#include <vector>

using namespace std;

// Definition for a Node.
class Node {
 public:
  int val;
  vector<Node*> children;

  Node() {}

  Node(int _val, vector<Node*> _children) {
    val = _val;
    children = _children;
  }
};

class Solution {
 public:
  vector<int> postorder(Node* root) {
    if (root == nullptr) {
      return vector<int>();
    }
    vector<int> result;
    for (int i = 0; i < root->children.size(); i++) {
      vector<int> child_post_order = postorder(root->children.at(i));
      for (int j = 0; j < child_post_order.size(); j++) {
        result.push_back(child_post_order.at(j));
      }
    }
    result.push_back(root->val);
    return result;
  }
};
