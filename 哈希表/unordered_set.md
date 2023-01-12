# unordered_set

## 性质

- unordered_set 容器提供了和 unordered_map 相似的能力，但 unordered_set 可以用保存的元素作为它们自己的键。T 类型的对象在容器中的位置由它们的哈希值决定，因而需要定义一个 Hash< T > 函数。基本类型可以省去Hash< T >方法。


- 不能存放重复元素。


- 可指定buckets个数，可进行初始化，也可后期插入元素


- 1、无序集是一种容器，它以不特定的顺序存储惟一的元素，并允许根据元素的值快速检索单个元素。
- 2、在unordered_set中，元素的值同时是唯一标识它的键。键是不可变的，只可增删，不可修改
- 3、在内部，unordered_set中的元素没有按照任何特定的顺序排序，而是根据它们的散列值组织成桶，从而允许通过它们的值直接快速访问单个元素(平均时间复杂度为常数)。
- 4、unordered_set容器比set容器更快地通过它们的键访问单个元素，尽管它们在元素子集的范围迭代中通常效率较低。
- 5、容器中的迭代器至少是前向迭代器。

```C++
std::unordered_set<string> example;
std::unordered_set<string> things {16}; // 16 buckets
std::unordered_set<string> words {"one", "two", "three", "four"};// Initializer list
std::unordered_set<string> copy_wrds {words}; // Copy constructor
```

## 成员函数

### 构造

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210717003455782.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MzY3OTAzNw==,size_16,color_FFFFFF,t_70)

### 迭代器

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210717003522776.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MzY3OTAzNw==,size_16,color_FFFFFF,t_70)

### 其余操作

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210717003552665.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MzY3OTAzNw==,size_16,color_FFFFFF,t_70)

### 查找

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210717003952108.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MzY3OTAzNw==,size_16,color_FFFFFF,t_70)

注意：如果没有匹配的元素，返回结束迭代器(set.end())

### 擦除

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210717004026295.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MzY3OTAzNw==,size_16,color_FFFFFF,t_70)

## 案例代码

```C++
void Sub_1()
{
	cout << "unordered_set测试" << endl;
	vector<int> nums1 = { 1,2,3,4,5,6 };
	unordered_set<int> set1(nums1.begin(), nums1.end());	//使用vector初始化set
	for (int num : set1)	//C++新特性 遍历容器中的每一个成员
	{
		cout << num << endl;
	}

	cout << "查找元素6" << endl;
	cout << *set1.find(6) << endl;	//.find返回的是一个地址 如果没找到返回结束迭代器
	if (set1.find(7) == set1.end())
	{
		cout << "没有查找到7" << endl;
		cout << *set1.find(7) << endl;
	}
}

```

![image-20220116222516001](https://happygoing.oss-cn-beijing.aliyuncs.com/img/image-20220116222516001.png)

