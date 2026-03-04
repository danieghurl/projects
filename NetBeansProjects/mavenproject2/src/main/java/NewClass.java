import java.util.*;

class MyStack{
    Stack<Integer>s;
    Integer minEle;
    
    MyStack(){s = new Stack<Integer>();}
    
    {
        if(s.isEmpty())
            System.out.println("Stack is empty");
        else
            System.out.println("Minimum Element in the"
                                         +"stack is:"+minEle);
    }
    void peek()
    {
        if(s.isEmpty()){
            System.out.println("Stack is empty");
            return;
        }
        Integer t = s.peek();
        System.out.println("Top Most Element is ");
        
        if(t<minEle)
            System.out.println(minEle);
        else 
            System.out.println(t);
    }
    
    {
        if(s.isEmpty()){
            System.out.println("Stack is empty");
            return;
    }
        System.out.println("Top Most Element Removed: ");
        Integer t = s.pop();
        
        if(t<minEle){
            System.out.println(minEle);
            minEle = 2*minEle - t;
        }
            else
                System.out.println(t);
}
    
    {
        if(s.isEmpty()){
            minEle = x;
            s.push(x);
            System.out.println("Number Inserted:"+x);
            return;
        }
        if(x<minEle){
            s.push(2*x-minEle);
            minEle = x;
        }
        else
            s.push(x);
        
        System.out.println("Number Inserted:"+x);
    }
}
