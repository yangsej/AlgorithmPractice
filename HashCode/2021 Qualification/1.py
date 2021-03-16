import sys

filename = sys.stdin.readline().strip()
sys.stdin = open("./HashCode 2021/" + filename + ".txt", "r")
sys.stdout = open("./HashCode 2021/" + filename + ".out.txt", "w")

# Duration, Intersections , Streets, Cars, Points
D, I, S, V, F = map(int, sys.stdin.readline().split()) 

class Car:
    def __init__(self, arr):
        self.P = arr[0]
        self.path = [streets[a] for a in arr[1:]]
        self.time = sum(map(int, self.path))
    
    def change(self):
        self.time -= int(self.path.pop(0))

class Street:
    count = 0
    def __init__(self, B: int, E: int, name: str,  L: int):
        self.B = int(B) # Begin
        self.E = int(E) # End
        self.name = name
        self.L = int(L) # Length
        self.time = 0 # schedule duration

        self.set()

    def __str__(self) -> str:
        return "%s %i" %(self.name, self.time)

    def __repr__(self) -> str:
        return "%s %i" %(self.name, self.time)
    
    def __eq__(self, o: str) -> bool:
        return self.name == o

    def __int__(self) -> int:
        return self.L

    def __add__(self, other) -> int:
        return self.L + other.L

    def set(self):
        intersections[self.B].set_out(self)
        intersections[self.E].set_in(self)


class Schedule:
    def __init__(self, street: Street, duration: int) -> None:
        self.street = street
        self.duration = duration
    
    def __str__(self) -> str:
        return "%s %i" % (self.street, self.duration)

    def __repr__(self) -> str:
        return "%s %i" % (self.street, self.duration)

class Intersection:
    count = 0
    def __init__(self, id):
        self.id = id
        self.income = [] # income streets
        self.schedule = [] # income streets duration schedule
        self.outcome = [] # outcome streets

    def __str__(self) -> str:
        return "%i\n%i\n" %(self.id, len(self.schedule)) + "".join(s + "\n" for s in self.schedule)

    def __repr__(self) -> str:
        return "%i\n%i\n" %(self.id, len(self.schedule)) + "".join(s + "\n" for s in self.schedule)

    def set_in(self, street: Street):
        self.income.append(street)
    
    def set_out(self, street: Street):
        self.outcome.append(street)

    def append(self, street, duration):
        if not self.schedule:
            Intersection.count += 1
        self.schedule.append(Schedule(street, duration))

    def check(self):
        current = [i for i in self.income]



intersections = [Intersection(i) for i in range(I)]
streets = {}
for s in range(S):
    B, E, name, L = sys.stdin.readline().split()
    streets[name] = Street(B, E, name, L)
cars = [Car(sys.stdin.readline().split()) for v in range(V)]













sys.stdout.write("%s\n" % str(Intersection.count))
sys.stdout.write("".join(map(str, intersections)))

# sys.stdout.write(A)
# for a in range(A):
#     sys.stdout.write(E)
#     for e in range(E):
#         sys.stdout.write(name + " " + T)