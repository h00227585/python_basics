from dataclasses import dataclass


@dataclass(frozen=True)
class Point3d:
    """
    定义三维空间的一个点
    """
    x: int
    y: int
    z: int

if __name__ == '__main__':
    point = Point3d(100, 200, 300)
    print(point) # 输出: Point3d(x=100, y=200, z=300)
    # 如果在PyCharm编辑器中尝试对point.x赋值会提示语法错误: 'Point3d'对象特性'x'为只读属性
    # point.x = 1000
