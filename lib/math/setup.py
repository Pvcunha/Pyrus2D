from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules = cythonize(["angle_deg.pyx",
                            "circle_2d.pyx",
                            "convex_hull.pyx",
                            "geom_2d.pyx",
                            "line_2d.pyx",
                            "math_values.pyx",
                            "matrix_2d.pyx",
                            "polygon_2d.pyx",
                            "ray_2d.pyx",
                            "rect_2d.pyx",
                            "region_2d.pyx",
                            "sector_2d.pyx",
                            "segment_2d.pyx",
                            "size_2d.pyx",
                            "soccer_math.pyx",
                            "triangle_2d.pyx",
                            "vector_2d.pyx"])
)

