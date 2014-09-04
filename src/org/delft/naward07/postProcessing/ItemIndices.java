package org.delft.naward07.postProcessing;

import java.util.ArrayList;
import java.util.List;

/**
 * Item indices.
 *
 * @author Feng Wang
 */
public class ItemIndices implements Comparable<ItemIndices> {

    /**
     * Number of the item.
     */
	private int num;

    /**
     * Indices of the item.
     */
	private List<Integer> indices;
	
	public ItemIndices(){
		num = 0;
		indices = new ArrayList<Integer>();
	}
	
	public void update(Integer index){
		num ++;
		indices.add(index);
	}
	
	public int getNum() { return num; }
	public List<Integer> getIndices() { return indices; }

	@Override
	public int compareTo(ItemIndices arg0) {
		// TODO Auto-generated method stub
		
		return this.getNum() < arg0.getNum() ? 1 : -1;
	}

}
