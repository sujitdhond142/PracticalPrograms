def fact(n)
	if n==1
		return 1
	else
		return n*fact(n-1)
	end
end
puts("Enter the number to find the factorial of the number :")
number = gets.to_i
puts(fact(number))
