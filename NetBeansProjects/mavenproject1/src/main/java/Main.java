import java.util.*;
class Stream {
List<Integer> nums;
Map<Integer, Set<Integer> > mp;
public Stream()
{
nums = new ArrayList<>();
mp = new HashMap<>();
}
public boolean insert(int val)
{
nums.add(val);
int index = nums.size() - 1;
if (!mp.containsKey(val)) {
mp.put(val, new HashSet<>());
}
mp.get(val).add(index);
return mp.get(val).size() == 1;
}
public boolean remove(int val)
{
if (!mp.containsKey(val)) {
return false;
}
Set<Integer> valIndices = mp.get(val);
int index = valIndices.iterator().next();
int lastIndex = nums.size() - 1;
valIndices.remove(index);
if (index != lastIndex) {
int lastNum = nums.get(lastIndex);
mp.get(lastNum).remove(lastIndex);
mp.get(lastNum).add(index);
Collections.swap(nums, index, lastIndex);
}
nums.remove(lastIndex);
if (valIndices.size() == 0) {
mp.remove(val);
}
return true;
}
public int getRandom()
{
int randomIndex
= (int)(Math.random() * nums.size());
return nums.get(randomIndex);
}
}
public class Main {
public static void main(String[] args)
{
Stream myStream = new Stream();
System.out.println(myStream.insert(5));
System.out.println(myStream.insert(6));
System.out.println(myStream.insert(5));
System.out.println(myStream.remove(6));
System.out.println(myStream.remove(6));
System.out.println(myStream.getRandom());
}
}