#2d uzaydaki noktaları içeren tuple
points = [(2,6),(3,4),(6,8),(9,2),(7,10)]

#öklid mesafesi için oluşturulan fonksiyon
def euclideanDistance(point1, point2):
    kare_farki = ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) 
    mesafe = kare_farki ** 0.5
    return mesafe

#nokta çiftleri arasındaki mesafeleri içeren "distances" adlı liste
distances = []
for i in range (len(points)):
    for j in range (i + 1, len(points)):
        distances.append((points[i], points[j], euclideanDistance(points[i], points[j])))

#minimum değeri bulma
min_distance = min(distances, key = lambda x: x[2])
print("iki nokta arasi minimum mesafe: ",min_distance)