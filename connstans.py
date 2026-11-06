import math

#доли компонентов
beton_1:float=0.15 #цемент
beton_2:float=0.35 #песок
beton_3:float=0.50 #щебень

keramika_1:float=0.60 #глина
keramika_2:float=0.25 #песок
keramika_3:float=0.15 #добавка

splav_1:float=0.70 #Cu
splav_2:float=0.25 #Zn
splav_3:float=0.05 #Pb

#допустимый диапозон массы
m_min:float=1.0
m_max:float=10000.0

#границы партий
mal:float=100.0 #<100 малая партия
bol:float=1000.0 #>1000 крупная партия

LOG_FILE: str = "input_errors.log"