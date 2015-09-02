#include <iostream>
#include <stack>
#include <stdio.h>
using namespace std;



struct node
{
	int data;
	struct node *left;
	struct node *right;

	node(int d) :data(d), left(NULL), right(NULL){}
};

node *NewNode(int d)
{
	return new node(d);
}
bool isPairPresentUtil(node *t1, node *t2, int sum)
{
	stack <node* > s1;
	stack <node* > s2;

	while (1)    {
		while (t1)   {
			s1.push(t1);
			t1 = t1->left;
		}
		while (t2)   {
			s2.push(t2);
			t2 = t2->right;
		}

		if (s1.empty() || s2.empty())
			return false;

		if ((s1.top())->data + (s2.top())->data == sum)
		{
			printf("%d %d", s1.top()->data, s2.top()->data);

			return true;
		}
		if ((s1.top())->data + (s2.top())->data > sum)
		{
			t2 = s2.top(); s2.pop();
			t2 = t2->left;
		}
		if ((s1.top())->data + (s2.top())->data < sum)
		{
			t1 = s1.top(); s1.pop();
			t1 = t1->right;
		}

	}
}
bool isPairPresent(node *t, int sum)
{
	return isPairPresentUtil(t, t, sum);
}
void testfindpair()
{
	struct node *root = NewNode(15);
	root->left = NewNode(10);
	root->right = NewNode(20);
	root->left->left = NewNode(8);
	root->left->right = NewNode(12);
	root->right->left = NewNode(16);
	root->right->right = NewNode(25);

	int target = 26;
	if (isPairPresent(root, target) == false)
		printf("\n No such values are found\n");

}

int main() {
	testfindpair();
	return 0;
}
