/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* reverseList(struct ListNode* head) {
    struct ListNode *temp=NULL;
    struct ListNode *prev=NULL;
    struct ListNode *current=head;
    while(current!=0){
        temp=current->next;
        current->next=prev;
        prev=current;
        current=temp; 
    }
    return prev;
}