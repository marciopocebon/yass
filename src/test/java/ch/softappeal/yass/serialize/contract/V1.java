package ch.softappeal.yass.serialize.contract;

import ch.softappeal.yass.util.Tag;

@Tag(120) public final class V1 {

  @Tag(1) public final int i1;

  public V1(final int i1) {
    this.i1 = i1;
  }

}
