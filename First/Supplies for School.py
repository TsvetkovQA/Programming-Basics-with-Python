pen_count = int(input())
markers_count = int(input())
detergent = int(input())
discount = int(input())
price_pen = pen_count * 5.80
price_markers = markers_count * 7.20
price_detergent = detergent * 1.20
price_for_all = price_pen + price_markers + price_detergent
discounted_price = price_for_all - (price_for_all * discount / 100)
print(discounted_price)
