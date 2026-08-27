/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* middleNode(struct ListNode* head) {
    struct ListNode *f;
    struct ListNode *s;
    f=head;
    s=head;
    while (f!=0 && f->next!=0){
        f=f->next->next;
        s=s->next;
    }
    return s;
}