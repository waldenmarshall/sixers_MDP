function coefficient = multinomial_coefficient(multiplicities)
    n = sum(multiplicities);  % Total number of elements in the multiset
    k = length(multiplicities);  % Number of distinct elements in the multiset

    coefficient = factorial(n) / prod(factorial(multiplicities));
end