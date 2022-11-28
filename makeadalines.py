import random, sys
for index, argument in enumerate(sys.argv):
        if index == 1:
                lines_to_gen=int(argument)

for i in range(lines_to_gen):
    satisfaction=random.randrange(1,6)
    food_quality=random.randrange(1,6)
    delivery=random.randrange(1,6)
    increment_string=str(i)
    satisfaction_review=(f"'satisfactionLOREMIPSUM {increment_string}'")
    food_quality_review=(f"'food qualityLOREMIPSUM {increment_string}'")
    deliver_review=(f"'deliveryLOREMIPSUM {increment_string}'")
    # num =< 42  then no rating
    # num =< 70 then all 3 categories
    # num =< 100 then only satisfaction
    choose_rating=random.randrange(1,101)
    choose_review=random.randrange(1,101)
    # No rating
    if choose_rating<=42:
        continue
    # All 3 categories rated
    elif choose_rating<=70:
        # No review
        if choose_review<=50:
            print(f"INSERT into rating (order_id,satisfaction,food_quality,delivery) VALUES ({id+i},{satisfaction},{food_quality},{delivery});")
        # Review
        else:
            print(f"INSERT into rating (order_id,satisfaction,food_quality,delivery,satisfaction_review,food_quality_review,delivery_review) VALUES ({id+i},{satisfaction},{food_quality},{delivery},{satisfaction_review},{food_quality_review},{deliver_review});")
    # Only satisfaction
    elif choose_rating<=100:
        # No review
        if choose_review<=50:
            print(f"INSERT into rating (order_id,satisfaction) VALUES ({id+i},{satisfaction});")
        # Review
        else:
            print(f"INSERT into rating (order_id,satisfaction,satisfaction_review) VALUES ({id+i},{satisfaction},{satisfaction_review});")
print("UPDATE orders INNER JOIN rating ON orders.id=rating.order_id SET orders.order_rating_id=rating.id;")