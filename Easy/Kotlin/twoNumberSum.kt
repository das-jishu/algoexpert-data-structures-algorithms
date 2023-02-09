@file:JvmName("Main")
fun main()
{
    println("result is ${twoNumberSum(intArrayOf(1,-1,5,-2),3).contentToString()}")
}

// O(N) time and space
fun twoNumberSum(array:IntArray,targetSum:Int):IntArray {
    if(array.size<2) return intArrayOf()
    val set = mutableSetOf<Int>()
    for(element in array)
    {
        if(set.contains(targetSum - element))
            return intArrayOf(element,targetSum - element)
        else
            set.add(element)    
    }

    return intArrayOf()
}

/* O(N^2) time, O(1) space
run two for loops and compare every pair to see if it matches.

O(N logN) time and O(1) space
sort the array first and then use the two pointer approach to find the target sum. */
