#include "n-ary-tree-postorder-traversal.cpp"
#include <gtest/gtest.h>
#include <vector>

using namespace std;

TEST(PostOrderTraversal, NoChildren) {
  Node n = Node(1, vector<Node*>());
  ASSERT_EQ(vector<int>{1}, Solution().postorder(&n));
}

TEST(PostOrderTraversal, OneChild) {
  Node child = Node(2, vector<Node*>());
  Node n = Node(1, vector<Node*>{&child});
  auto expected = vector<int>{2, 1};
  ASSERT_EQ(expected, Solution().postorder(&n));
}

int main(int argc, char** argv) {
  testing::InitGoogleTest(&argc, argv);
  return RUN_ALL_TESTS();
}
