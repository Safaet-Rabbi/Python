face_count = {
    "Tetrahedron": 4,
    "Cube": 6,
    "Octahedron": 8,
    "Dodecahedron": 12,
    "Icosahedron": 20
}
n =int(input())
total_faces = 0
for _ in range(n):
    polyhedron_name = input().strip()
    total_faces += face_count[polyhedron_name]
print(total_faces) 