package ch.softappeal.yass.tutorial.contract;

import java.math.BigInteger;
import java.util.ArrayList;
import java.util.List;

public final class Node {

    public final BigInteger id;
    public final List<Node> links = new ArrayList<>();

    public Node(final long id) {
        this.id = BigInteger.valueOf(id);
    }

}
