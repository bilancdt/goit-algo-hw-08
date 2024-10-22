import heapq

def min_cost_to_connect_cables(cables):
    # Ініціалізуємо мін-купу з початковими довжинами кабелів
    heapq.heapify(cables)
    
    total_cost = 0
    
    # Поки в купі більше одного кабеля, продовжуємо об'єднувати
    while len(cables) > 1:
        # Вибираємо два найкоротші кабелі
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)
        
        # Витрати на їх об'єднання
        cost = first + second
        total_cost += cost
        
        # Додаємо новий кабель назад в купу
        heapq.heappush(cables, cost)
    
    return total_cost


cables = [4, 3, 2, 6,8,10,17,5,7,24]
result = min_cost_to_connect_cables(cables)
print(f"Мінімальні витрати на об'єднання кабелів: {result}")
