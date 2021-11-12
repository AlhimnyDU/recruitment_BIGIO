import java.io.*;
import java.util.*;
public class Main
{
  static class ListNode {

        int data;
        ListNode next;

        // Constructor
        ListNode(int d)
        {
            data = d;
            next = null;
        }
    }

	static public int detectLoop(ListNode head)
  {
    ListNode tortoise = head;
    ListNode hare = head;
    while(hare.next!=null&&hare!=null)
    {
        tortoise=tortoise.next;
        hare=hare.next.next;
        if(hare==tortoise)
        return 1;
    }
    return 0;
  }

  public static void main(String[] args) {
	    int[] num = {10, 20, 30, 40};

      	int k = detectLoop(num);
		System.out.println(k);
	}
}

