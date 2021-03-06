function x = Nearest(birds)
 
[~,b] = size(birds);
x = 1:b;
 
for i=1:b                   %Para cada passaro do bando.
    %Calcula a dist�ncia euclidiana para cada um dos outros passaros e
    %identifica o passaro que est� mais pr�ximo.
    best = inf;
    for j=1:b               %para todos os passaros
        if i ~= j           %exceto ele mesmo
            %Calcula a dist�ncia euclidiana.
            dist = sqrt((birds(1,i)-birds(1,j))^2+(birds(2,i)-birds(2,j))^2+(birds(3,i)-birds(3,j))^2);
            if best>dist        %Se � menor que a j� existente
                x(i) = j;       %Substitui.
                best = dist;
            end
        end
    end
    if best>1
        x(i)=i;
    end
end
