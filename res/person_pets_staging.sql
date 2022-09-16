select
	p.id,
	p.name,
	p.age,
	p.gender,
	pet1.name pet1_name,
	pet1.age pet1_age,
	pet1.gender pet1_gender,
	pet1.kind pet1_kind,
	pet2.name pet2_name,
	pet2.age pet2_age,
	pet2.gender pet2_gender,
	pet2.kind pet2_kind,
	pet3.name pet3_name,
	pet3.age pet3_age,
	pet3.gender pet3_gender,
	pet3.kind pet3_kind
from
	person p
	left join pet pet1
		on p.pet_1 = pet1.id
	left join pet pet2
		on p.pet_2 = pet2.id
	left join pet pet3
		on p.pet_3 = pet3.id
