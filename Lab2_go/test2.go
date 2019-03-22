package main

import (
	"fmt"
	"time"
	"math/rand"
)

// основная функция - в ней задается канал, вызываются горутины и ставится таймаут на прекращение вещания
func main() {
	// тип данных канал (спец тип данных в го). создается без доп опций, содержит инты
	intCh := make(chan int)

	// запуск пишущей в канал рутины, передается канал как аргумент
	go wrt(intCh)
	// запуск обрабатывающей рутины, передается тот же самый канал
	go read(intCh)
	// тайм аут и сообщение о прекращении вещания
	time.Sleep(100000000000)
	println("finish")
}

// горутина транслятор, принимает канал для записи
func wrt(ch chan int){
	// бесконечный цикл (типа while true)
	for {
		// генерится рандомное число и помещается в канал
		ch <- rand.Intn(5)
		// таймаут чтобы не было бегущей строки (время исчисляется в наносекундах)
		time.Sleep(1000000000)
	}
}

// горутина обработчик, принимает тот же самый канал
func read(ch chan int){
	// промежуточный результат. динамический массив нулевой длины
	result := make([]int, 0)
	// счетчик длины текущего массива
	counter := 0
	// бесконечный цикл
	for {
		// если текущий массив заполнен
		if counter == 0{
			// если в массиве есть числа выводим
			if len(result) > 0 {
				// вывод массива в консоль
				fmt.Println(result)
			}
			// обнуляем массив результата
			result = make([]int, 0)
			// помещаем в каунтер длину нового массива
			counter = <-ch
			// выводим для контроля
			fmt.Println(counter)
		// если массив еще не заполнен
		}else{
			// забираем пришедшее число из канала и добавляем его в текущий массив
			result = append(result, <-ch)
			// уменьшаем счетчик
			counter --
		}
	}
}
